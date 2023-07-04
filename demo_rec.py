from datetime import datetime
#import configparser
import vlc
import cv2
from mqttclient import MqttClient
import time

clientname = 'odbiornik_1'

mqttIP = '127.0.0.1'
mqttPort = 1883
mqttUsername = 'mqtt-test'
mqttPassword = 'mqtt-test'

Topic = 'synchro_test'

sample_msg = {"type": "REQUEST", "id": clientname}

def callback(client, topic, msg):
    
    if msg["type"]=="REQUEST":
        print("Odebrano komunikat")
        print("Odtwarzam plik")
        movie = "NAGRANIE FHD.mp4"




if __name__ == '__main__':
        
    try:    
        client = MqttClient(clientname, mqttIP, port=mqttPort)
        client.start([Topic], callback, block=False)
        print('Connected to the MQTT server')
        print('Client id: ', clientname)
    except:
        print ('Error while connecting to the MQTT server!')


    try:
        while True:
                            
            time.sleep(1)
            
    except KeyboardInterrupt:
        client.stop()
        pass        