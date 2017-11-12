#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

DEBUG = True
GREEN = True

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GREEN_LED = 18
RED_LED = 23
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

LED_CHECK_FREQ = 4


def loop():

    global GREEN

    if GREEN:
        print('Green on')
        GPIO.output(GREEN_LED, True)
        GPIO.output(RED_LED, False)
        time.sleep(LED_CHECK_FREQ)
        GREEN = False
    else:
        print('Green off')
        GPIO.output(GREEN_LED, False)
        GPIO.output(RED_LED, True)
        time.sleep(LED_CHECK_FREQ)
        GREEN = True

    time.sleep(LED_CHECK_FREQ)

if __name__ == '__main__':
    try:
        print 'Press Ctrl-C to quit.'
        while True:
            loop()
    finally:
        GPIO.cleanup()

