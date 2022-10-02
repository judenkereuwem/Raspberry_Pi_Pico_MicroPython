from machine import Pin, I2C
import utime
from pico_i2c_lcd import I2cLcd
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

def ultrasonic():
    timepassed = 0
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    while echo.value() == 0:
        signaloff = utime.ticks_us()
    while echo.value() ==1:
        signalon = utime.ticks_us()
    timepassed = signalon - signaloff
    return timepassed
while True:
    measured_time = ultrasonic()
    distance_cm = (measured_time * 0.0343)/2
    distance_cm = round(distance_cm, 2)
    print(distance_cm)
    lcd.move_to(0, 0)
    lcd.putstr("Distance: ")
    lcd.move_to(10, 0)
    lcd.putstr(str(distance_cm))
    lcd.move_to(14, 0)
    lcd.putstr("cm")
    if distance_cm > 99:
        lcd.move_to(10, 0)
        lcd.putstr("100+     ")
    utime.sleep(0.5)
