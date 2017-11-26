import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# switch
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# LED
GPIO.setup(19, GPIO.OUT)

def loop():
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')
        GPIO.output(19, True)
        time.sleep(0.5)
        GPIO.output(19, False)
        time.sleep(0.1)

if __name__ == '__main__':
    try:
        print 'Press Ctrl-C to quit.'
        while True:
            loop()
    finally:
        GPIO.cleanup()