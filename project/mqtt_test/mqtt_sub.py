#subscribe
import paho.mqtt.client as mqtt

host='172.17.0.2'
port=1883
data=0.00
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
        print('eq')
    else:
#        print('1')
        data=new_data
#    print(data)
        a=getdata()
#    print(a)
	
   # print(msg.topic+" "+str(msg.payload))
def getdata():
    print(data)
    return data
if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host, port, 60)
    client.loop_forever()
