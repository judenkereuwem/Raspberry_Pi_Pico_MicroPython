import machine
import utime
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

sensor_temp = machine.ADC(4)
conversion_factor = 3.3/(65535)

while True:
    reading = sensor_temp.read_u16()*conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)

    oled.fill(0)
    oled.text("Temp: ", 0, 16)
    oled.text(str(round(temperature, 2)), 48, 16) 
    oled.text("*C", 96, 16)
    utime.sleep(0.5)
    oled.show()