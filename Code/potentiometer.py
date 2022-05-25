from machine import ADC, Pin, PWM
import time

pwm = PWM(Pin(15))
adc = ADC(Pin(26))

pwm.freq(1000)

while True:
    #print(adc.read_u16())
    #time.sleep(1)
    duty = adc.read_u16()
    pwm.duty_u16(duty)