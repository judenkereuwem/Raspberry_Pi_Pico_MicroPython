from machine import Pin
from time import sleep

led = Pin(25, Pin.OUT)

while True:
    led.value(1)
    sleep(1)
    led.value(0)
    sleep(1)