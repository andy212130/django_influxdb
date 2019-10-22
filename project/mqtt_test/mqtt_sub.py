#subscribe
import paho.mqtt.client as mqtt
from random import random

host='172.17.0.2'
port=1883
data= format(random()*30, '.2f')

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("aaa")

def on_message(client, userdata, msg):
    new_data=msg.payload
    global data
#    new_data=new_data.split('\'')
#    print(new_data)
#    print('#')
#    print(data)
    if data==new_data:
        text ='eq'
#        print(text)
    else:
#        print('1')
        data=new_data
#    print(data)
#        a=getdata()
#    print(a)
	
   # print(msg.topic+" "+str(msg.payload))
def getdata():
    print(data)
    return data

def start():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host, port, 60)
    client.loop_start()
    return getdata()

#def stop():
#    client.loop_stop()


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host, port, 60)
    client.loop_forever()
