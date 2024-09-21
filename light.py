import board
import busio
import adafruit_bh1750
from adafruit_bme280 import basic
from digitalio import DigitalInOut, Direction
from time import sleep

# power up the uŠup connector
uSup_power = DigitalInOut(board.IO3)
uSup_power.direction = Direction.OUTPUT
uSup_power.value = 1
# wait for the pull-up resistors to do their job
sleep(0.05)

# create the I2C bus object
i2c = busio.I2C(board.IO18, board.IO19)

# create sensor objects
sensor_light = adafruit_bh1750.BH1750(i2c)
sensor_air = basic.Adafruit_BME280_I2C(i2c)

# read sensor data
while True:
    print("Light:", round(sensor_light.lux, 1), "lux |",
          "Temperature:", round(sensor_air.temperature, 1), "°C |",
          "Rel. humidity", round(sensor_air.relative_humidity, 1), "% |",
          "Pressure:", round(sensor_air.pressure, 1), "hPa")
    sleep(0.5)
