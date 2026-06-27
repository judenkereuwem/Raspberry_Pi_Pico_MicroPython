from servo import Servo
from time import sleep

# Create a Servo object on pin 0
servo=Servo(pin=0)

    
try:
    while True:
        # Move from 0 to 180 degrees slowly
        for angle in range(0, 181, 1):  # step = 1 degree
            servo.move(angle)
            sleep(0.02)  # small delay between steps

        # Move back from 180 to 0 degrees slowly
        for angle in range(180, -1, -1):
            servo.move(angle)
            sleep(0.02)

except KeyboardInterrupt:
    print("Keyboard interrupt")
    # Turn off PWM 
    servo.stop()