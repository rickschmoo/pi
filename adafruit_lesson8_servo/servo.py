Last login: Sun Nov 12 14:35:34 on ttys001
➜  ~ ssh 192.168.7.79
The authenticity of host '192.168.7.79 (192.168.7.79)' can't be established.
ECDSA key fingerprint is SHA256:pQwFBZ46Ez1Yq1rJsryn0pdibEBzI1FJ/ouMS14ZY2A.
Are you sure you want to continue connecting (yes/no)? yes
Warning: Permanently added '192.168.7.79' (ECDSA) to the list of known hosts.
rboardman@192.168.7.79's password:
Permission denied, please try again.
rboardman@192.168.7.79's password:
Permission denied, please try again.
rboardman@192.168.7.79's password:

➜  ~ ssh pi@192.168.7.79
pi@192.168.7.79's password:
Permission denied, please try again.
pi@192.168.7.79's password:
Permission denied, please try again.
import RPi.GPIO as GPIO
pi@192.168.7.79's password:

➜  ~ ssh pi@192.168.7.79
pi@192.168.7.79's password:

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/*/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
#!/usr/bin/env python
permitted by applicable law.
Last login: Sun Nov 12 14:32:03 2017
pi@raspberrypi:~ $ ls
Desktop  Documents  Music         Pictures  python_games  Videos
dev      Downloads  oldconffiles  Public    Templates
pi@raspberrypi:~ $ ls
Desktop  Documents  Music         Pictures  python_games  Videos
#!/usr/bin/env python
dev      Downloads  oldconffiles  Public    Templates
pi@raspberrypi:~ $ cd dev
pi@raspberrypi:~/dev $ ls
pi@raspberrypi:~/dev $ mkdir basic_led
pi@raspberrypi:~/dev $ cd basic_led/
pi@raspberrypi:~/dev/basic_led $ ls
pi@raspberrypi:~/dev/basic_led $ vi led.py
pi@raspberrypi:~/dev/basic_led $ chmod u+x led.py
pi@raspberrypi:~/dev/basic_led $ ./led.py
import time
Press Ctrl-C to quit.
^CTraceback (most recent call last):
  File "./led.py", line 22, in <module>
    loop()
  File "./led.py", line 15, in loop
    GPIO.output(GREEN_LED, True)
KeyboardInterrupt
pi@raspberrypi:~/dev/basic_led $ vi led.py
pi@raspberrypi:~/dev/basic_led $ ./led.py

Press Ctrl-C to quit.
^CTraceback (most recent call last):
  File "./led.py", line 22, in <module>
    loop()
KeyboardInterrupt
pi@raspberrypi:~/dev/basic_led $ vi led.py
pi@raspberrypi:~/dev/basic_led $ ./led.py
Press Ctrl-C to quit.
Traceback (most recent call last):
#!/usr/bin/env python
  File "./led.py", line 38, in <module>
    loop()
  File "./led.py", line 21, in loop
    if GREEN:
UnboundLocalError: local variable 'GREEN' referenced before assignment
pi@raspberrypi:~/dev/basic_led $ vi led.py
pi@raspberrypi:~/dev/basic_led $ ./led.py
Press Ctrl-C to quit.
Traceback (most recent call last):
  File "./led.py", line 38, in <module>
    loop()
  File "./led.py", line 21, in loop
    if GREEN:
UnboundLocalError: local variable 'GREEN' referenced before assignment
pi@raspberrypi:~/dev/basic_led $ vi led.py
pi@raspberrypi:~/dev/basic_led $ ./led.py
Press Ctrl-C to quit.
Traceback (most recent call last):
  File "./led.py", line 38, in <module>
    loop()
  File "./led.py", line 21, in loop
    if GREEN:
UnboundLocalError: local variable 'GREEN' referenced before assignment
pi@raspberrypi:~/dev/basic_led $ vi led.py
pi@raspberrypi:~/dev/basic_led $ emacs
-bash: emacs: command not found
pi@raspberrypi:~/dev/basic_led $ vi led.py
pi@raspberrypi:~/dev/basic_led $ nano led.py
pi@raspberrypi:~/dev/basic_led $ nano led.py
pi@raspberrypi:~/dev/basic_led $ ./led.py
Press Ctrl-C to quit.
Traceback (most recent call last):
  File "./led.py", line 40, in <module>
    loop()
  File "./led.py", line 21, in loop
    if GREEN:
UnboundLocalError: local variable 'GREEN' referenced before assignment
pi@raspberrypi:~/dev/basic_led $ nano led.py
pi@raspberrypi:~/dev/basic_led $ ./led.py
  File "./led.py", line 7
    global GREEN = True
                 ^
SyntaxError: invalid syntax
pi@raspberrypi:~/dev/basic_led $ nano led.py
pi@raspberrypi:~/dev/basic_led $ ./led.py
Press Ctrl-C to quit.
Traceback (most recent call last):
  File "./led.py", line 41, in <module>
    loop()
  File "./led.py", line 22, in loop
    if GREEN:
UnboundLocalError: local variable 'GREEN' referenced before assignment
pi@raspberrypi:~/dev/basic_led $ nano led.py
pi@raspberrypi:~/dev/basic_led $ ./led.py
Press Ctrl-C to quit.
Green on
Green off
Green on
^CTraceback (most recent call last):
  File "./led.py", line 42, in <module>
    loop()
  File "./led.py", line 27, in loop
    time.sleep(LED_CHECK_FREQ)
KeyboardInterrupt
pi@raspberrypi:~/dev/basic_led $ nano led.py
pi@raspberrypi:~/dev/basic_led $ more led.py
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

pi@raspberrypi:~/dev/basic_led $ ./led.py
Press Ctrl-C to quit.
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
Green on
Green off
  GNU nano 2.2.6              File: servo.py

# Servo Control
import time
import wiringpi

# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()

# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.01

while True:
        for pulse in range(50, 250, 1):
                wiringpi.pwmWrite(18, pulse)
                time.sleep(delay_period)
        for pulse in range(250, 50, -1):
                wiringpi.pwmWrite(18, pulse)
                time.sleep(delay_period)

