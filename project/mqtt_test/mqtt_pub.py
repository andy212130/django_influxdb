#publisher
import paho.mqtt.client as mqtt
from random import random
import time
_g_cst_ToMQTTTopicServerIP = "172.17.0.2"#host
_g_cst_ToMQTTTopicServerPort = 1883 #port
_g_cst_MQTTTopicName = "aaa" #TOPIC name
while True:
	data = random() *30
	print(data)
	mqttc = mqtt.Client("python_pub")
	mqttc.connect(_g_cst_ToMQTTTopicServerIP, _g_cst_ToMQTTTopicServerPort)
	mqttc.publish(_g_cst_MQTTTopicName, data)
	time.sleep(5)
