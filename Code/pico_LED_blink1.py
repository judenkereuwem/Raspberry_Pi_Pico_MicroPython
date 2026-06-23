from machine import Pin
from time import sleep

led = Pin(20, Pin.OUT)

while True:
    led.value(1)
    print("on")
    sleep(2)
    led.value(0)
    print("off")
    sleep(2)