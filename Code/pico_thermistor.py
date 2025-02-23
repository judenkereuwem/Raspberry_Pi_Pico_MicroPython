from machine import ADC, Pin
import utime
import math

#Variable declaration
logR2 = None
R2 = None
T = None
Tc = None
Tf = None

R1 = 10000
c1 = 1.009249522e-03
c2 = 2.378405444e-04
c3 = 2.019202697e-07

thermistorPin = machine.ADC(27)

while True:
    reading = thermistorPin.read_u16()

    R2 = R1 * (65535 / reading - 1.0);
    logR2 = math.log(R2);
    T = (1.0 / (c1 + c2*logR2 + c3*logR2*logR2*logR2));
    Tc = T - 273.15;
    Tf = (Tc * 9.0)/ 5.0 + 32.0;

    print("Temperature: ", Tc)
    print("Temperature: ", Tf)
    print(" ")
    utime.sleep(0.5)
