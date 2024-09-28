import analogio
import time
import config


def initialize_battery_voltage_reader(vbat_pin):
    """
    initialize VBAT pin object for measuring battery object.
    """
    
    battery_voltage_reader = analogio.AnalogIn(vbat_pin)
    time.sleep(0.2)
    return battery_voltage_reader


def read_battery_voltage(battery_voltage_reader):
    """
    Read battery voltage from VBAT pin object.
    """
    
    raw_reading = battery_voltage_reader.value
    # values are returned as 16-bit (CircuitPython implementation) and must be converted to 12-bit (the real ESP32-C3 ADC bit depth)
    voltage = (raw_reading / 65536 * 4096) * config.VBAT_DIVIDER_RATIO / 1000
    
    return {
        "battery_raw_reading": str(raw_reading),
        "battery_voltage": str(round(voltage, 3)),
    }


def print_battery_voltage(battery_voltage):
      """
      Print battery voltage data.
      """
      
      print("Battery voltage:", battery_voltage["battery_voltage"], "V |",
            "Raw reading:", battery_voltage["battery_raw_reading"])

