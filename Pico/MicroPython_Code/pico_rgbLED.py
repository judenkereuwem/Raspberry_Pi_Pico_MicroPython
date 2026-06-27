from picozero import RGBLED
from time import sleep

rgb = RGBLED(red = 16, green = 17, blue = 18)

while True:
    rgb.color = (255, 0, 0)
    sleep(0.5)
    rgb.color = (0, 255, 0)
    sleep(0.5)
    rgb.color = (0, 0, 255)
    sleep(0.5)
    rgb.color = (0, 0, 0)
    sleep(0.5)

    # blink purple 2 seconds, off 0.5 seconds
    #rgb.blink((0.5, 0.5, 0.5), colors=((255, 0, 0), (0, 255, 0), (0, 0, 255)), wait=True, n=3)
    #print("Finished blinking") # Runs after 3 repeats

    # Colour cycle slower in the opposite direction
    #rgb.cycle(fade_times=3, colors=((0, 0, 255), (0, 255, 0), (255, 0, 0)), wait=True, n=2)

    # 2 second to fade from purple to off, 0.5 seconds to change from off to purple
    #rgb.pulse(fade_times=(2, 0.5), colors=((0, 0, 255), (255, 0, 0)), wait=True, n=2)
    #print("Finished pulsing") # Runs after 3 pulses

    #rgb.off()