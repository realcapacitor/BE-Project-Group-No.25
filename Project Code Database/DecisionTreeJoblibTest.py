#Thu 13 Mar 12:27 PM
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib
import random
import csv
import datetime
from paho.mqtt import client as mqtt_client
broker = 'localhost' #<---
port = 1883
inTopic = "inTopic"

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
# username = 'emqx'
# password = 'public'
########################################################################
####Send back workplace####





def sendback(onOff):
    if onOff == 0:
        client.publish(outTopic, 0)
    elif onOff ==1:
        client.publish(outTopic, 1)


########################################################################
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
            data  = msg.payload.decode()
            with open('data.csv', mode='a', newline='') as csv_file:
                writer = csv.writer(csv_file)
    
    # get current time and format as string
                now = datetime.datetime.now()
                timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")
                datalist = data.split(', ')
                moisture = float(datalist[0])
                irrigation = 0
                

                # write data to CSV file with timestamp
                writer.writerow([timestamp_str, moisture, irrigation])
            
            
            
            


    client.subscribe(inTopic)
    client.on_message = on_message


def run():
    global client 
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()


if __name__ == '__main__':
    run()

################################################

