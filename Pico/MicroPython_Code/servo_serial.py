
    
from servo import Servo
from time import sleep
import sys

# Initialize servo
servo = Servo(pin=0)
moving = False  # Flag to control motion

def smooth_move():
    global moving
    while moving:
        for angle in range(30, 160, 1):
            if not moving:
                return
            servo.move(angle)
            check_command_non_blocking()
            sleep(0.1)

        for angle in range(160, 30, -1):
            if not moving:
                return
            servo.move(angle)
            check_command_non_blocking()
            sleep(0.1)

def check_command_non_blocking():
    import select
    if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        command = sys.stdin.readline().strip().lower()
        handle_command(command)

def handle_command(command):
    global moving
    if command == "start":
        if not moving:
            moving = True
            smooth_move()
    elif command == "stop":
        moving = False
        servo.stop()

# Main loop
print("Waiting for PC commands...")

while True:
    try:
        command = sys.stdin.readline().strip().lower()
        handle_command(command)
    except Exception as e:
        print("Error:", e)

