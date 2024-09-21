import time

import config
from connect_wifi import connect_wifi
from mqtt import setup_mqtt_client, send_mqtt_message, format_mqtt_payload
from sensors import initialize_sensors, print_sensor_data, read_sensor_data


# Connect to WiFi network
connect_wifi(config.WIFI_SSID, config.WIFI_PASSWORD)

# Set up MQTT client
mqtt_client = setup_mqtt_client(config.MQTT_IP, config.MQTT_PORT)

# Connect the client to the MQTT broker
print("Connecting to MQTT broker...")
mqtt_client.connect()

# Initialize I2C BUS and sensors
sensor_air, sensor_light = initialize_sensors(config.POWER_UP_PIN, config.SCL_PIN, config.SDA_PIN)


while True:
    # read sensor data
    measurements = read_sensor_data(sensor_light, sensor_air)
    
    # print sensor data for debug
    print_sensor_data(measurements)

    # compose MQTT message
    message = format_mqtt_payload(measurements)

    # send message to broker
    send_mqtt_message(mqtt_client, config.MQTT_FEED, message)

    # sleep 
    # TODO: go to deep sleep
    time.sleep(config.MEASUREMENT_INTERVAL)
