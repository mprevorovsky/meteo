import os
import board


WIFI_SSID = os.getenv('CIRCUITPY_WIFI_SSID')
WIFI_PASSWORD = os.getenv("CIRCUITPY_WIFI_PASSWORD")

MQTT_IP = "192.168.1.112"
MQTT_PORT = 1883
MQTT_FEED = "greenhouse/meteo"

POWER_UP_PIN = board.IO3
SCL_PIN = board.IO18
SDA_PIN = board.IO19

VBAT_PIN = board.IO0
VBAT_DIVIDER_RATIO = 1.7693877551 # https://github.com/LaskaKit/Meteo_Mini/blob/main/SW/Meteo_Mini_ADC/Meteo_Mini_ADC.ino

MEASUREMENT_INTERVAL = 30
