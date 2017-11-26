# LED on GPIO 19
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(19, GPIO.OUT)

while (True):
  GPIO.output(19, True)
  time.sleep(0.5)
  GPIO.output(19, False)
  time.sleep(0.5)