from machine import Pin
import utime

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

def ultrasonic():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() == 1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed * 0.0343) / 2
    distance = round(distance, 2) 
    print("Distance: ", distance, "cm")
    
while True:
    ultrasonic()
    utime.sleep(1)