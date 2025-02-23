from machine import ADC, Pin
from time import sleep

LDR = ADC(Pin(26))

while True:
    light = LDR.read_u16()
    light = int(light/65535*100)
    print(light)
    sleep(0.5)

