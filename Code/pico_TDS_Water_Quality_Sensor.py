from machine import ADC, Pin
from picozero import LED
import time

# Connect TDS sensor output to GP26 (ADC0)
tds_adc = ADC(Pin(26))

# Example alert LED (on GP15)
alert_led = LED(15)

# Calibration values
VREF = 3.3       # Pico ADC reference voltage
K_VALUE = 0.5    # Probe calibration constant
TEMP = 28        # Assume 25°C water temp

def read_tds():
    # Read 16-bit value (0–65535) from ADC
    raw = tds_adc.read_u16()
    voltage = (raw / 65535) * VREF  # Convert to volts

    # Temperature compensation
    comp_coeff = 1.0 + 0.02 * (TEMP - 25.0)
    comp_voltage = voltage / comp_coeff

    # Convert voltage to TDS (ppm)
    tds = (133.42 * comp_voltage**3
          - 255.86 * comp_voltage**2
          + 857.39 * comp_voltage) * K_VALUE

    return tds, voltage

while True:
    tds, volt = read_tds()
    print("Voltage: {:.2f} V | TDS: {:.2f} ppm".format(volt, tds))

    # Example: Turn on LED if water is poor quality
    if tds > 1000:
        alert_led.on()
    else:
        alert_led.off()

    time.sleep(1)
