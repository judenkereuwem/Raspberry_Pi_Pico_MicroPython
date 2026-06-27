from machine import ADC, Pin
import time

# Initialize ADC (use the pin where the pH sensor analog output is connected)
ph_sensor = ADC(Pin(26))  # GP26 (ADC0)

# Reference voltage of Pico ADC
VREF = 3.3
ADC_RESOLUTION = 65535  # 16-bit for MicroPython on Pico

# Calibration values (you must calibrate with buffer solutions)
# Example: Voltage values at pH 4.0 and pH 7.0
voltage_at_pH4 = 1.92   # volts (example, measure in your setup)
voltage_at_pH7 = 2.50   # volts (example, measure in your setup)

# Calculate slope
slope = (7.0 - 4.0) / (voltage_at_pH7 - voltage_at_pH4)

def read_ph():
    # Read raw ADC value
    raw = ph_sensor.read_u16()
    voltage = (raw / ADC_RESOLUTION) * VREF
    
    # Convert voltage to pH using calibration
    ph_value = 7.0 + (voltage - voltage_at_pH7) * slope
    return ph_value, voltage

while True:
    ph, v = read_ph()
    print("pH: {:.2f} | Voltage: {:.2f} V".format(ph, v))
    time.sleep(1)
