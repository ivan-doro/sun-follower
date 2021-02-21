import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

import Servos
import LDRs

servos = Servos.Servos()
ldrs = LDRs.LDRs
 
try:
    for i in range (10):
        #read LDRs: [up, down, right, left]
        lightVal = ldrs.read()  #[2, 2.5, 2.6, 3]
        print(lightVal)
        if (sum(lightVal)/4 < 3.2): #if it's too dark, no point looking for the sun

            # move up/down until the perfect position
            while(abs(lightVal[0] - lightVal[1]) > 0.1):
                try:
                    print("up: ", lightVal[0], ", down: ", lightVal[1])
                    if(lightVal[0] - lightVal[1] > 0):
                        servos.moveDown()
                        print("move down")
                    elif(lightVal[0] - lightVal[1] < 0):
                        servos.moveUp()
                        print("moveUp")
                        
                    lightVal = ldrs.read() # update sensor read
#                     time.sleep(3)
                except Exception as e:
                    print(e)
                    break
                
            # move up/down until the perfect position
            while(abs(lightVal[2] - lightVal[3]) > 0.1):
                try:
                    print("right: ", lightVal[2], ", left: ", lightVal[3])
                    if(lightVal[2] - lightVal[3] > 0):
                        servos.moveLeft()
                        print("moveLeft")
                    elif (lightVal[2] - lightVal[3] < 0):
                        servos.moveRight()
                        print("moveRight")
                        
                    lightVal = ldrs.read() # update sensor read
#                     time.sleep(3)

                except Exception as e:
                    print(e)
                    break
 
        print("next")
        time.sleep(7)
except KeyboardInterrupt:
    print("turning off")
 
GPIO.cleanup() 