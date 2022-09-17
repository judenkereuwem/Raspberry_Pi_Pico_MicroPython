
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from machine import RTC

#Initialize I2C and OLED
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

while True:
    
    #Initialize RTC
    rtc = RTC()
    date = rtc.datetime()[0:3]
    time = rtc.datetime()[4:7]
    
    print("Time: ", ':'.join(str(x) for x in time))

    oled.fill(0)
    oled.text("Pico Clock ", 20, 8)
    oled.text(':'.join(str(x) for x in time), 20, 30)
    oled.text("am", 85, 30)
    oled.show()

