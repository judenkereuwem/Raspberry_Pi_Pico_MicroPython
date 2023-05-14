from machine import Pin, ADC
import utime

xAxis = ADC(Pin(27))
yAxis = ADC(Pin(26))
button = Pin(16,Pin.IN, Pin.PULL_UP)
currentStatus = ""

while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value()
    xStatus = "middle"
    yStatus = "middle"
    buttonStatus = "not pressed"
    
    #print("X: ", xValue)
    #print("Y: ", yValue)
    #print("")
    
    if yValue <= 30000:
        xStatus = "left"
    elif yValue >= 60000:
        xStatus = "right"
    if xValue >= 60000:
        yStatus = "up"
    elif xValue <= 30000:
        yStatus = "down"
    if buttonValue == 0:
        buttonStatus = "pressed"
    #print("X: " + xStatus + ", Y: " + yStatus + " -- button " + buttonStatus)
    
    
    if xStatus is not "middle" and yStatus == "middle" and buttonStatus == "not pressed":
        currentStatus = xStatus
    elif yStatus is not "middle" and xStatus == "middle" and buttonStatus == "not pressed":
        currentStatus = yStatus
    elif xStatus == "middle" and yStatus == "middle" and buttonStatus == "pressed":
        currentStatus = buttonStatus
    elif xStatus == "middle" and yStatus == "middle" and buttonStatus == "not pressed":
        currentStatus = "nothing"
        
    print(currentStatus)
        
    utime.sleep(0.1)
    
    