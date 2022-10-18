from machine import ADC, Pin, I2C
import time
import framebuf
from ssd1306 import SSD1306_I2C

adc = ADC(Pin(26))

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

while True:
    
    adc0 = int((adc.read_u16() / 65536) * 101)
    adcstr = str(adc0)
    print(adcstr)
    oled.text(adcstr + "%", 15, 0, 1)
    oled.hline(15, 20, 99, 1)
    oled.hline(15, 28, 99, 1)
    oled.vline(14, 20, 9, 1)
    oled.vline(114, 20, 9, 1)
    oled.fill_rect(15, 20, adc0, 8, 1)
    oled.show()
    time.sleep(0.05)
    oled.fill(0)

