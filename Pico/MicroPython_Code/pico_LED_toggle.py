from machine import Pin
led = Pin(25, Pin.OUT)

#led.value(1) #led on
#led.value(0) #led off
led.toggle() #led on/off when Run is pressed