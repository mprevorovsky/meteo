import busio
import time
import adafruit_bh1750
from adafruit_bme280 import basic
from digitalio import DigitalInOut, Direction


def _power_up_connector(power_up_pin):
      """
      Power up the uŠup connector.
      """

      uSup_power = DigitalInOut(power_up_pin)
      uSup_power.direction = Direction.OUTPUT
      uSup_power.value = 1
      
      # wait for the pull-up resistors to do their job
      time.sleep(0.05)


def initialize_sensors(power_up_pin, scl_pin, sda_pin):
      """
      Initialize sensor objects for BME280 and BH1750.
      """

      # power up the sensors
      _power_up_connector(power_up_pin)
      
      # create an I2C bus object
      i2c = busio.I2C(scl_pin, sda_pin)

      # create sensor objects
      sensor_light = adafruit_bh1750.BH1750(i2c)
      sensor_air = basic.Adafruit_BME280_I2C(i2c)

      return sensor_air, sensor_light



def print_sensor_data(light_intensity, temperature, humidity, air_pressure):
      """
      Print light intensity, temperature, humidity and air_pressure.
      """
      
      print("Light:", light_intensity, "lux |",
          "Temperature:", temperature, "°C |",
          "Rel. humidity", humidity, "% |",
          "Pressure:", air_pressure, "hPa")


def read_sensor_data(sensor_light, sensor_air):
    """
    Read light intensity, temperature, humidity and air pressure data from sensors.
    """
    
    light_intensity = str(round(sensor_light.lux, 1))
    temperature = str(round(sensor_air.temperature, 1))
    humidity = str(round(sensor_air.relative_humidity, 1))
    air_pressure = str(round(sensor_air.pressure, 1))

    return light_intensity, temperature, humidity, air_pressure

