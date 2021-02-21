#Program for continuous motion of 2 servos
#wiring:
#white - signal, middle black - Vcc, side black - GND
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
# setting up pin 3 to control servo with pwm
GPIO.setup(3, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
servo_frequency = 1 / 0.02 #20ms is pulse period for the servo (f = 1/period[s])
pwm0 = GPIO.PWM(3, servo_frequency)
pwm1 = GPIO.PWM(17, servo_frequency)

dc = 7.5 #7.5 #middle position
pwm0.start(dc) #% of duty cycle, this motor has range 0.5-2.5 ms -> 2.5% - 12.5%
pwm1.start(dc) #% of duty cycle, this motor has range 0.5-2.5 ms -> 2.5% - 12.5%
time.sleep(1)
pwm0.ChangeDutyCycle(dc)
pwm1.ChangeDutyCycle(dc)

#initialazing cycle (to bring servos to netral position)
for i in range (75, 50, -1):
    dc = i/10
    pwm0.ChangeDutyCycle(dc)
    pwm1.ChangeDutyCycle(dc)
    time.sleep(0.05)
    
pwm0.ChangeDutyCycle(0)
pwm1.ChangeDutyCycle(0)
time.sleep(1)

for i in range (50, 100, 1):
    dc = i/10
    pwm0.ChangeDutyCycle(dc)
    pwm1.ChangeDutyCycle(dc)
    time.sleep(0.05)

pwm0.ChangeDutyCycle(0)
pwm1.ChangeDutyCycle(0)
time.sleep(1)

for i in range (100, 74, -1):
    dc = i/10
    pwm0.ChangeDutyCycle(dc)
    pwm1.ChangeDutyCycle(dc)
    time.sleep(0.05)

pwm0.ChangeDutyCycle(0)
pwm1.ChangeDutyCycle(0)
time.sleep(1)
# try:
#     t = 0.5
#     while True:
#        
#         #print('ADC Voltage 0: ' + str(ch0.voltage) + 'V')
#         #print('ADC Voltage 1: ' + str(ch1.voltage) + 'V')
#        
#         
#         dc = dc + t
#         if(dc > 12 or dc < 3):
#             t = -t
#        
#         print(dc)
#         pwm0.ChangeDutyCycle(dc)
#         pwm1.ChangeDutyCycle(dc)
# 
#         time.sleep(1)
#         
# except KeyboardInterrupt:
#     print("ending program")

   
pwm0.stop()
pwm1.stop() 
GPIO.cleanup()