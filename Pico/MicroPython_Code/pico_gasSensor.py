# from machine import Pin
# import utime
# 
# gasSensor = Pin(16, Pin.IN, Pin.PULL_UP)
# 
# while True:
#     print(gasSensor.value())
#     if gasSensor.value() == 1:
#         print("gas not detected")
#         utime.sleep(0.2)
#     else:
#         print("gas detected")
#         utime.sleep(0.2)
        
        
        
#------- Analog Gas Sensor reading ----------#
from machine import ADC, Pin
import utime

adc = ADC(Pin(26))

while True:
    print(adc.read_u16())
    utime.sleep(0.5)