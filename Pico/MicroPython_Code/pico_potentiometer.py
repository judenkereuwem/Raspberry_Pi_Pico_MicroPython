
from machine import ADC, Pin
import time

adc = ADC(Pin(28))

while True:
    print(adc.read_u16())
    time.sleep(1)
