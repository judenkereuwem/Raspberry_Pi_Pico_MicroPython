from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

# OLED display
i2c = I2C(0, sda=Pin(16), scl=Pin(17), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

# Tilt sensor: first pin to VCC and the other to GP2
tilt = Pin(2, Pin.IN, Pin.PULL_DOWN)

while True:
    oled.fill(0)
    if tilt.value() == 1:
        oled.text("Flat", 50, 20)
    elif tilt.value() == 0:
        oled.text("Vertical", 30, 20)
    oled.show()