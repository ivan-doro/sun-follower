#Support file for MainController, that controlls servo
#Wiring:
#white - signal, middle black - Vcc, side black - GND
#GPIO: 3(up-down), 17(right-left)

#Servo positions:                 
midPos0 = 7.5 # NOT USED
midPos1 = 7.5 # NOT USED
minDC = 6
maxDC = 9

#const
changeDcTime = 0.1 #waiting time for servo movement
dcStep = 0.05 #Duty Cycle step for move functions

#setup
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)



class Servos:
    
    #global variables declaration
    dc0 = 0
    dc1 = 0
    pwm0 = 0
    pwm1 = 0
    
    def __init__(self):
        global dc0, dc1, pwm0, pwm1
        
        # setting up pins to control servo with pwm
        GPIO.setup(3, GPIO.OUT) # UP-DOWN
        GPIO.setup(17, GPIO.OUT) # RIGHT_LEFT
        servo_frequency = 1 / 0.02 #20ms is pulse period for the servo (f = 1/period[s])
        pwm0 = GPIO.PWM(3, servo_frequency) 
        pwm1 = GPIO.PWM(17, servo_frequency) 

        #set initial Duty Cycles
        dc0 = 7.5 # up(12.5) - down(2.5)
        dc1 = 7.5 # right(2.5) - left(12.5)
        pwm0.start(dc0) #% of duty cycle, this motor has range 0.5-2.5 ms -> 2.5% - 12.5%
        pwm1.start(dc1) #% of duty cycle, this motor has range 0.5-2.5 ms -> 2.5% - 12.5%
        
        #initialazing cycle (to bring servos to netral position)
        for i in range (75, minDC*10, -1):
            dc0 = i/10
            dc1 = i/10
            pwm0.ChangeDutyCycle(dc0)
            pwm1.ChangeDutyCycle(dc1)
            time.sleep(changeDcTime)
        for i in range (minDC*10, maxDC*10, 1):
            dc0 = i/10
            dc1 = i/10
            pwm0.ChangeDutyCycle(dc0)
            pwm1.ChangeDutyCycle(dc1)
            time.sleep(changeDcTime)

        for i in range (maxDC*10, 74, -1):
            dc0 = i/10
            dc1 = i/10
            pwm0.ChangeDutyCycle(dc0)
            pwm1.ChangeDutyCycle(dc1)
            time.sleep(changeDcTime)
            
        pwm0.ChangeDutyCycle(0)
        pwm1.ChangeDutyCycle(0)
        
    def moveDown(self):
        global dc0, pwm0
        if (dc0 > minDC):
            dc0 = dc0 - dcStep
            
            pwm0.ChangeDutyCycle(dc0)
            time.sleep(changeDcTime)
            pwm0.ChangeDutyCycle(0)
            time.sleep(changeDcTime)
        else:
            raise Exception("Out of range (down)")

    def moveUp(self):
        global dc0, pwm0
        if (dc0 < maxDC):
            dc0 = dc0 + dcStep
            
            pwm0.ChangeDutyCycle(dc0)
            time.sleep(changeDcTime)
            pwm0.ChangeDutyCycle(0)
            time.sleep(changeDcTime)
        else:
            raise Exception("Out of range (up)")
        
    def moveRight(self):
        global dc1, pwm1
        if (dc1 < maxDC):
            dc1 = dc1 + dcStep
            
            pwm1.ChangeDutyCycle(dc1)
            time.sleep(changeDcTime)
            pwm1.ChangeDutyCycle(0)
            time.sleep(changeDcTime)
        else:
            raise Exception("Out of range (right)")
        
    def moveLeft(self):
        global dc1, pwm1
        if (dc1 > minDC):
            dc1 = dc1 - dcStep
            
            pwm1.ChangeDutyCycle(dc1)
            time.sleep(changeDcTime)
            pwm1.ChangeDutyCycle(0)
            time.sleep(changeDcTime)
        else:
            raise Exception("Out of range (left)")
            