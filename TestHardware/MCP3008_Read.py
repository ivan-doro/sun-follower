#Tutorial:
#https://learn.adafruit.com/reading-a-analog-in-and-controlling-audio-volume-with-the-raspberry-pi?view=all

#Connection:
#1,2(red) - Vcc; 3,8(black) - GND;
#4(ylw) - SCLK(P11); 5(purp) - MISO(P9); 6(orng) - MOSI(P10); 7(grn) - P22;
import RPi.GPIO as GPIO
import os
import time
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
chTest = AnalogIn(mcp, MCP.P1)
ch3 = AnalogIn(mcp, MCP.P3) #2nd photoresistor
ch4 = AnalogIn(mcp, MCP.P4) #3nd photoresistor
ch5 = AnalogIn(mcp, MCP.P5) #4nd photoresistor

 
# setting up pin 12 to control servo with pwm
GPIO.setup(12, GPIO.OUT)
servo_frequency = 1 / 0.02 #20ms is pulse period for the servo
pwm = GPIO.PWM(12, servo_frequency)
 
dc = 7.5 #middle position
pwm.start(dc)
time.sleep(1)
 
try:
    while True:
        photoR2 = ch2.voltage
        photoR3 = ch3.voltage
        photoR4 = ch4.voltage
        photoR5 = ch5.voltage
        #print(chTest.voltage)
       
        print('V2: ' + str(photoR2) + 'V, V3: '+ str(photoR3) + 'V, V4: '+ str(photoR4) + 'V, V5: '+ str(photoR5))
       
        #if(ch0.voltage - ch1.voltage < -0.2 and dc < 12.5):
        #    dc = dc + 0.5
        #elif(ch0.voltage - ch1.voltage > 0.2 and dc > 2.5):
        #    dc = dc - 0.5
       
        #print(dc)
        #pwm.ChangeDutyCycle(dc)
        time.sleep(2)
       
except KeyboardInterrupt:
    print("ending program")
   
pwm.stop()
GPIO.cleanup() 