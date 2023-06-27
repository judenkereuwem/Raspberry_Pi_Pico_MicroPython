from machine import Pin
from time import sleep

a = Pin(10, Pin.OUT)
b = Pin(11, Pin.OUT)
c = Pin(12, Pin.OUT)
d = Pin(13, Pin.OUT)
e = Pin(14, Pin.OUT)
f = Pin(15, Pin.OUT)
g = Pin(16, Pin.OUT)

while True:
    # number 0
    a.value(1)    
    b.value(1)
    c.value(1)
    d.value(1)
    e.value(1)
    f.value(1)
    g.value(0)
    sleep(1)
    
    # number 1
    a.value(0)    
    b.value(1)
    c.value(1)
    d.value(0)
    e.value(0)
    f.value(0)
    g.value(0)
    sleep(1)
    
    # number 2
    a.value(1)    
    b.value(1)
    c.value(0)
    d.value(1)
    e.value(1)
    f.value(0)
    g.value(1)
    sleep(1)
    
    # number 3
    a.value(1)    
    b.value(1)
    c.value(1)
    d.value(1)
    e.value(0)
    f.value(0)
    g.value(1)
    sleep(1)
    
    # number 4
    a.value(0)    
    b.value(1)
    c.value(1)
    d.value(0)
    e.value(0)
    f.value(1)
    g.value(1)
    sleep(1)
    
    # number 5
    a.value(1)    
    b.value(0)
    c.value(1)
    d.value(1)
    e.value(0)
    f.value(1)
    g.value(1)
    sleep(1)
    
    # number 6
    a.value(1)    
    b.value(0)
    c.value(1)
    d.value(1)
    e.value(1)
    f.value(1)
    g.value(1)
    sleep(1)
    
    # number 7
    a.value(1)    
    b.value(1)
    c.value(1)
    d.value(0)
    e.value(0)
    f.value(0)
    g.value(0)
    sleep(1)
    
    # number 8
    a.value(1)    
    b.value(1)
    c.value(1)
    d.value(1)
    e.value(1)
    f.value(1)
    g.value(1)
    sleep(1)
    
    # number 9
    a.value(1)    
    b.value(1)
    c.value(1)
    d.value(1)
    e.value(0)
    f.value(1)
    g.value(1)
    sleep(1)
