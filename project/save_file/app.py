#!/usr/bin/python3.6
# -*- coding: UTF-8 -*-

import serial, time
import json
import datetime
from serial import SerialException
import paho.mqtt.client as mqtt
import socket

# MQTT setup data
MQTT_SERVER = "127.0.0.1" #"10.20.0.19"
MQTT_PORT = 1883
MQTT_TOPIC = "air-conditioner-vent"

cold_sensor = serial.Serial()
# socket setup data
bind_ip = "192.168.8.101"
send_port = 9808

send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
send_socket.connect((bind_ip,send_port))
a = '{"active":"create","cmd":"./subscriber -DCPSConfigFIle rtps.ini","topic":"A"}'
send_socket.send(a.encode())
print (send_socket.recv(1024))

while(1):
	# b = '{"send":{"from":"7610307082307919","message":"dfsfs"}}'
	b = '{"send":"{\\"from\\":\\"7610307082307919\\",\\"message\\":\\"dfsfs\\"}"}'
	print(b)
	send_socket.send(a.encode())
	b_json = json.loads(b)
	b_split = json.dumps(b_json)
	print(b_json['send'])
	send_socket.send(b.encode())
	print (send_socket.recv(1024))

	if(cold_sensor.is_open):
		send_status = 0
		response = cold_sensor.readline()
		response = response.decode('ascii')
		print(response)
#		response = '{"Temperature" : "30.5", "Humidity" : "100"}'
		try:
			data = json.loads(str(response))
			Temperature = data["Temperature"]
			Humidity = data["Humidity"]
			Temperature = float(Temperature)
#			print(Temperature, type(Temperature), Humidity, type(Humidity))
			send_status = 1
		except:
			send_status = 0
		print('------------------------------------------------------')
		if (send_status == 1):
			try:
				# MQTT connection
				mqtt_conn = mqtt.Client()
				mqtt_conn.connect(MQTT_SERVER, MQTT_PORT)
				mqtt_conn.publish(MQTT_TOPIC, response)
				now = datetime.datetime.now()
				print('MQTT To Server OK ! -->' , now)
			except:
				print('MQTT To Server Error !')
		print('------------------------------------------------------')
		time.sleep(1)
	else:
		try:
			cold_sensor = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
			time.sleep(2.5)
		except:
			cold_sensor = serial.Serial()
		time.sleep(1)
