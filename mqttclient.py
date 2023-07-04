"""MQTT client for BIOPUAP."""


import json
import threading
import datetime
import logging
from typing import Callable, Union, Any
from base64 import b64encode, b64decode
import paho.mqtt.client as mqtt
import cv2
import vlc
log = logging.getLogger(__name__)


class DataEncoder(json.JSONEncoder):
    """Encodes dict into JSON data. Supports binary data (encode to base64)
    and datetime (encodes to isoformat).
    """
    # pylint: disable=method-hidden

    def default(self, data):
        if isinstance(data, bytes):
            return b64encode(data).decode()
        elif isinstance(data, datetime.datetime):
            return data.isoformat()
        return json.JSONEncoder.default(self, data)


class MqttClient:
    """MQTT client communnicating with the broker."""

    def __init__(self, client_name: str, host: str, port: int = 1883,
                username: str = None, password: str = None) -> None:
        """Connect to the broker.
        client_name - must be UNIQUE!
        host, port - broker hostname and port
        username, password = broker credentials (optional).
        """
        self.client = mqtt.Client(client_name, userdata=self)
        if username is not None and password is not None:
            self.client.username_pw_set(username, password)
        self.client.on_message = self.on_message
        self.client.connect(host, port)
        self.callback = None
        self.topic = None
        self.thread = None

    def publish(self, topic: str, msg: dict) -> None:
        """Publish a message msg with a given topic."""
        try:
            if not isinstance(msg, str):
                msg = json.dumps(msg, cls=DataEncoder)
            self.client.publish(topic, msg)
        except Exception as e:
            # log all unhandled exceptions
            log.error('%s %s', type(e), e, exc_info=True)
            # raise  # for testing!

    def start(self, topic: Union[str, list, tuple],
                callback: Callable[[str, str, dict], None],
                block: bool = True) -> None:
        """Subscribe to the topic and start the message loop.
        topic - a single topic or a list of topics to subscribe
        callback - function(client, topic, msg) called for each message.
        block - if False, start the loop in a separate thread.
        """
        self.topic = topic
        self.callback = callback
        if isinstance(topic, (list, tuple)):
            for t in topic:
                self.client.subscribe(t)
        else:
            self.client.subscribe(topic)
        if block:
            self.client.loop_forever()
        else:
            self.thread = threading.Thread(target=self.client.loop_forever)
            self.thread.start()

    def stop(self) -> None:
        """Stop the message loops."""
        self.callback = None
        self.client.unsubscribe(self.topic)
        self.topic = None
        self.client.loop_stop()
        self.client.disconnect()
        if self.thread is not None:
            self.thread.join()
            self.thread = None

    def on_message(self, client: str, userdata: Any, msg: mqtt.MQTTMessage) -> None:
        """Callback for received messages."""
        if msg.retain == 1:
            return  # ignore retained messages
        try:
            data = json.loads(msg.payload.decode())
            if self.callback:
                self.callback(self, msg.topic, data)
        except Exception as e:
            # log all unhandled exceptions
            log.error('%s %s', type(e), e, exc_info=True)
            # raise  # for testing

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.client.disconnect()


def decode_binary_data(msg: dict) -> dict:
    """Decode message fields that were encoded in base64."""
    if not isinstance(msg, dict):
        return msg
    for key in ('BioParamsBinary', 'BioSignalsBinary'):
        if key in msg and isinstance(msg[key], str):
            msg[key] = b64decode(msg[key].encode())
    return msg
