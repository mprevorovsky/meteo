import os
import wifi
import time

import mqtt


WIFI_SSID = os.getenv('CIRCUITPY_WIFI_SSID')
WIFI_PASSWORD = os.getenv("CIRCUITPY_WIFI_PASSWORD")

MQTT_IP = "192.168.1.112"
MQTT_PORT = 1883


def connect_wifi():
    print(f"Connecting to {WIFI_SSID}")
    wifi.radio.connect(WIFI_SSID, WIFI_PASSWORD)
    print(f"Connected to {WIFI_SSID}!")


# MAIN
# Connect to WiFi network
connect_wifi()
# Set up MQTT client
mqtt_client = mqtt.setup_mqtt_client(MQTT_IP, MQTT_PORT)
# Connect the client to the MQTT broker.
print("Connecting to MQTT broker...")
mqtt_client.connect()

# Setup a feed for publishing
meteo_feed = "greenhouse/temperature"


temperature_val = 0

while True:
    # Send message
    print(f"Sending sensor values: {temperature_val}...")
    mqtt_client.publish(meteo_feed, temperature_val)
    print("Sent!")
    temperature_val += 1
    time.sleep(5)
