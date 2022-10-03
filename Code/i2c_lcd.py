from machine import I2C, Pin
from time import sleep
from pico_i2c_lcd import I2cLcd
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

I2C_ADDR = i2c.scan()[0]
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

# -------------- Test Area ------------------- #


#lcd.backlight_off()
#while True:
msrg = 3

lcd.putstr("Message: "+str(msrg))  
#lcd.putstr("Placidlearn")

#lcd.blink_cursor_on()
#lcd.move_to(2,0)
#lcd.putstr("Follow for more"+"\n")
#lcd.putstr("")

   
