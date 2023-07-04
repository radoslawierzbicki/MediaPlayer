from datetime import datetime
#import configparser
import vlc
import screeninfo
import runpy
import cv2
from mqttclient import MqttClient
import time

clientname = 'nadawca'

mqttIP = '127.0.0.1'
mqttPort = 1883
mqttUsername = 'mqtt-test'
mqttPassword = 'mqtt-test'

Topic = 'synchro_test'

sample_msg = {"type": "REQUEST", "id": clientname}

def callback(client, topic, msg):
    
    msg=msg

if __name__ == '__main__':

        
    try:    
        client = MqttClient(clientname, mqttIP, port=mqttPort)
        client.start([Topic], callback, block=False)
        print('Connected to the MQTT server')
        print('Client id: ', clientname)
    except:
        print ('Error while connecting to the MQTT server!')


    time.sleep(5)
#######CHECK-IN MESSAGE#######

    curDate = datetime.utcnow().isoformat() + "Z"
    sample_msg["time"] = curDate
    
    sample_msg["movie"] = "NAGRANIE FHD.mp4"

    try:

        print (sample_msg)
        client.publish(Topic, sample_msg)
        print('Message sent')
        movie = "C:/Users/asus/Desktop/projekt/Projekt/pythonProject3/NAGRANIE FHD.mp4"
        vlc_instance = vlc.Instance()

        player = vlc_instance.media_player_new()
        player.set_mrl(movie)
        player.set_fullscreen(True)
        player.play()

        #runpy.run_path(path_name='C:/Users/Radek/PycharmProjects/pythonProject3/main.py')

        # wait so the video can be played for 5 seconds
        # irrespective for length of video
        time.sleep()



    except:
        print ('Error while sending the check-in message!')

##############################   
          
    time.sleep(2)
    client.stop()