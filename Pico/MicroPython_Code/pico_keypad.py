from machine import Pin
import utime

led = Pin(15, Pin.OUT)

col_list = [1,2,3,4]
row_list = [5,6,7,8,9]

for x in range(0, 5):
    row_list[x] = Pin(row_list[x], Pin.OUT)
    row_list[x].value(1)
    
for x in range(0, 4):
    col_list[x] = Pin(col_list[x], Pin.IN, Pin.PULL_UP)

key_map = [["LEFT","0","RIGHT","ENT"],\
          ["7","8","9","ESC"],\
          ["4","5","6","DOWN"],\
          ["1","2","3","UP"],\
          ["F1","F2","#","*"]]

def Keypad4x5Read(cols, rows):
    for r in rows:
        r.value(0)
        result = [cols[0].value(),cols[1].value(),cols[2].value(),cols[3].value()]
        if min(result)==0:
            key=key_map[int(rows.index(r))][int(result.index(0))]
            r.value(1) #manages key kept pressed
            return(key)
        r.value(1)
        
print("----Ready for user inputs-------")
while True:
    key=Keypad4x5Read(col_list, row_list)
    if key != None:
        print("Input: "+key)
        led.value(1)
        utime.sleep(0.3)
        led.value(0)