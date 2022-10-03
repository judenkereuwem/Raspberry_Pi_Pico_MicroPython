from machine import ADC, Pin
import utime

analog_value = machine.ADC(28)
convertion_factor = 3.3/(65535)

while True:
    reading = analog_value.read_u16()
    voltage_value = reading * convertion_factor
    print("ADC values: ", reading)
    print("Voltage:    ",voltage_value)
    print(" ")
    utime.sleep(0.5)
