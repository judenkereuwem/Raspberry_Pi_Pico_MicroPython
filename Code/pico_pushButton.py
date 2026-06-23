from picozero import Button
from time import sleep

button = Pin(10, Pin.IN, Pin.PULL_UP)

while True:
    if button.is_pressed:
        print("Button is pressed")
    else:
        print("Button is not pressed")
    sleep(0.1)
    


# from machine import Pin
# import time
# 
# # configure pin 15 as input with pull-down resistor
# button = Pin(1, Pin.IN, Pin.PULL_DOWN)
# 
# while True:
#     if button.value() == 1:   # HIGH = pressed
#         print("Button is pressed")
#     else:
#         print("Button is not pressed")
#     time.sleep(0.1)
