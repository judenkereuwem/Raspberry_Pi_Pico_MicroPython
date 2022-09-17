
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from machine import RTC

#Initialize I2C and OLED
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
oled = SSD1306_I2C(128, 64, i2c)

#Initialize RTC
rtc = RTC()
date = rtc.datetime()[0:3]
time = rtc.datetime()[4:6]

#print(rtc.datetime())
#print("Date: ", *date)
#print("Time: ", *time)

print("Date: ", '-'.join(str(x) for x in date))
print("Time: ", ':'.join(str(x) for x in time))


oled.text("Date: ", 0, 16)
oled.text(':'.join(str(x) for x in date), 48, 16)
oled.text("Time: ", 0, 30)
oled.text(':'.join(str(x) for x in time), 48, 30)
oled.show()

