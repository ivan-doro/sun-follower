import time
import board
from digitalio import DigitalInOut, Direction

RCpin1 = board.D18
RCpin2 = board.D25

i = 0
sumReading1 = 0
sumReading2 = 0
while i < 100:
    i += 1
    with DigitalInOut(RCpin1) as rc:
        reading1 = 0
        
        rc.direction = Direction.OUTPUT
        rc.value = False
        
        time.sleep(0.1)
        
        rc.direction = Direction.INPUT
        
        while rc.value is False:
            reading1 += 1
        
    
    with DigitalInOut(RCpin2) as rc:
        reading2 = 0
        
        rc.direction = Direction.OUTPUT
        rc.value = False
        
        time.sleep(0.1)
        
        rc.direction = Direction.INPUT
        
        while rc.value is False:
            reading2 += 1
            
    sumReading1 += reading1
    sumReading2 += reading2
    if(i % 5 == 0):
        avgReading1 = sumReading1 / 5
        sumReading1 = 0
        avgReading2 = sumReading2 / 5
        sumReading2 = 0
        print ("1: " + str(avgReading1) + ",    2: " + str(avgReading2 / 0.95)) #1, 1.75, 2.95, 1.1, 1.69, 1.93
        time.sleep(1)
#0: 