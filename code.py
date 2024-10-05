import time

import config
from connect_wifi import connect_wifi
from mqtt import setup_mqtt_client, send_mqtt_message, format_mqtt_payload
from sensors import initialize_sensors, print_sensor_data, read_sensor_data
from battery import initialize_battery_voltage_reader, read_battery_voltage, print_battery_voltage


# Connect to WiFi network
connect_wifi(config.WIFI_SSID, config.WIFI_PASSWORD)

# Set up MQTT client
mqtt_client = setup_mqtt_client(config.MQTT_IP, config.MQTT_PORT)

# Connect the client to the MQTT broker
print("Connecting to MQTT broker...")
mqtt_client.connect()

# Initialize I2C BUS and sensors
sensor_light_VEML770, sensor_air = initialize_sensors(config.POWER_UP_PIN, config.SCL_PIN, config.SDA_PIN)

# Initialize VBAT pin for reading battery voltage
battery_voltage_reader = initialize_battery_voltage_reader(config.VBAT_PIN)


while True:
    # read sensor data and battery voltage
    sensor_measurements = read_sensor_data(sensor_light_VEML770, sensor_air)
    battery_voltage_data = read_battery_voltage(battery_voltage_reader)
    
    # print sensor and voltage data for debug
    print_sensor_data(sensor_measurements)
    print_battery_voltage(battery_voltage_data)

    # compose MQTT message
    message = format_mqtt_payload(sensor_measurements | battery_voltage_data)

    # send message to broker
    send_mqtt_message(mqtt_client, config.MQTT_FEED, message)

    # sleep 
    # TODO: go to deep sleep
    time.sleep(config.MEASUREMENT_INTERVAL)
