from machine import ADC, Pin
from time import sleep

LM35 = ADC(Pin(26))

while True:
    reading = LM35.read_u16()
    voltage = (reading / 65535) * 3.3
    tempC = voltage*100
    tempF = (tempC*9.0/3.3)+32.0
    
    print("tempC", "%.2f" % tempC, "\xB0C")
    print("tempC", "%.2f" % tempF, "\xB0F")
    print("")
    sleep(0.5)