#Support file for MainController, that reads photocells
#Wiring:
#p0 - orange, p1 - yellow, p2 - green, p3 - purple


import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

import os
import busio
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn

#setting up analog read with mcp3008 chip
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.D22)
mcp = MCP.MCP3008(spi, cs)
ch2 = AnalogIn(mcp, MCP.P2) #1st photoresistor
ch3 = AnalogIn(mcp, MCP.P3) #2nd photoresistor
ch4 = AnalogIn(mcp, MCP.P4) #3nd photoresistor
ch5 = AnalogIn(mcp, MCP.P5) #4nd photoresistor

class LDRs:
    
    
    

    def read():
        global ch2
        global ch3
        global ch4
        global ch5
        
        #read LDR sensors
        photoR0 = ch2.voltage
        photoR1 = ch3.voltage
        photoR2 = ch4.voltage
        photoR3 = ch5.voltage
        #recalculate the values for correct orientation
        lightLeft = (photoR0 + photoR3)/2
        lightRight = (photoR1 + photoR2)/2
        lightUp = (photoR0 + photoR1)/2
        lightDown = (photoR2 + photoR3)/2
        
        #print ("up: ", lightUp, ", down: ", lightDown, ", r: ", lightRight, ", l: ", lightLeft)
        return [lightUp, lightDown, lightRight, lightLeft]

# for i in range (100):
#     val = LDRs.read()
#     time.sleep(1)