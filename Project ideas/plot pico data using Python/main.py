from machine import ADC, Pin
from time import sleep

photoRes = ADC(Pin(28))

while True:
    light = photoRes.read_u16()
    light = int(light/65535*100)
    print(light)
    sleep(0.5)


