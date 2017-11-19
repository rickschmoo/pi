import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)
 
MotorInput1 = 4 # PIN 7 GPIO 4
MotorInput2 = 17 # PIN 11 GPIO 17
MotorEnable = 18 # PIN 22 GPIO 18 (PWM CAPABLE)
 
GPIO.setup(MotorInput1,GPIO.OUT)
GPIO.setup(MotorInput2,GPIO.OUT)
GPIO.setup(MotorEnable,GPIO.OUT)
 
print "Turning motor forwards!"
GPIO.output(MotorInput1,GPIO.HIGH)
GPIO.output(MotorInput2,GPIO.LOW)
GPIO.output(MotorEnable,GPIO.HIGH)
 
sleep(2)

print "Stopping motor"
GPIO.output(MotorEnable,GPIO.LOW)

print "Turning motor backwards!"
GPIO.output(MotorInput1,GPIO.LOW)
GPIO.output(MotorInput2,GPIO.HIGH)
GPIO.output(MotorEnable,GPIO.HIGH)

sleep(2)

print "Stopping motor"
GPIO.output(MotorEnable,GPIO.LOW)


GPIO.cleanup()

