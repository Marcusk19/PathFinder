# Example code for using mqtt protocol

import paho.mqtt.publish as publish

MQTT_SERVER = "45.56.117.102" # ip address of linode instance
MQTT_PATH = "test_channel"

publish.single(MQTT_PATH, "Hello World!", hostname=MQTT_SERVER)
print("Published message to " + MQTT_SERVER)   