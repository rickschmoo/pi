import RPi.GPIO as GPIO
from time import sleep
 
GPIO.setmode(GPIO.BCM)
 
MotorInput1 = 4 # PIN 7 GPIO 4
MotorInput2 = 17 # PIN 11 GPIO 17
MotorEnable = 18 # PIN 22 GPIO 18 (PWM CAPABLE)
 
GPIO.setup(MotorInput1,GPIO.OUT)
GPIO.setup(MotorInput2,GPIO.OUT)
GPIO.setup(MotorEnable,GPIO.OUT)
pwm=GPIO.PWM(MotorEnable, 100)
pwm.start(0)

print "Set direction forwards ..."
GPIO.output(MotorInput1,GPIO.HIGH)
GPIO.output(MotorInput2,GPIO.LOW)

print "Forward at 25%"
pwm.start(0)
pwm.ChangeDutyCycle(25)
GPIO.output(MotorEnable,GPIO.HIGH)
sleep(2)

print "Stopping motor"
GPIO.output(MotorEnable,GPIO.LOW)
pwm.stop()
sleep(2)

###

print "Forward at 50%"
pwm.start(0)
pwm.ChangeDutyCycle(50)
GPIO.output(MotorEnable,GPIO.HIGH)
sleep(2)

print "Stopping motor"
GPIO.output(MotorEnable,GPIO.LOW)
pwm.stop()
sleep(2)

###

print "Forward at 100%"
pwm.start(0)
pwm.ChangeDutyCycle(100)
GPIO.output(MotorEnable,GPIO.HIGH)
sleep(2)

print "Stopping motor"
GPIO.output(MotorEnable,GPIO.LOW)


# cleanup
pwm.stop()
GPIO.cleanup()

