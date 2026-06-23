
from machine import Pin
import utime
import _thread

led1 = Pin(2, machine.Pin.OUT)
led2 = Pin(3, machine.Pin.OUT)
sLock = _thread.allocate_lock()

def second_thread():
    while True:
        sLock.acquire()
        led2.toggle()
        print("Second thread")
        utime.sleep(1)
        sLock.release()
_thread.start_new_thread(second_thread, ())

while True:
    # We acquire the semaphore lock
    sLock.acquire()
    led1.toggle()
    print("First thread")
    utime.sleep(1)
    # We release the semaphore lock
    sLock.release()