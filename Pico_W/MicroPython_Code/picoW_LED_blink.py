import machine
import time

led = machine.Pin('LED', machine.Pin.OUT)

while True:
    led.on()
    time.sleep(0.2)
    led.off()
    time.sleep(0.2)