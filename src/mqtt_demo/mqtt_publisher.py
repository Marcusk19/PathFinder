# Example code for using mqtt protocol

import paho.mqtt.publish as publish

MQTT_SERVER = "192.168.0.239"
MQTT_PATH = "test_channel"

publish.single(MQTT_PATH, "Hello World!", hostname=MQTT_SERVER)