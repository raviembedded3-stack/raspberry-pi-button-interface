#PULL_UP_WITH_LEVEL_TRIGGERING

import RPi.GPIO as GPIO
import time
#--------------------------------------------------------#
BUTTON_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#--------------------------------------------------------#
try:
    while True:
        state = GPIO.input(BUTTON_PIN)
        if state == 1:
            print("BUTTON NOT PRESSED..!")
        else:
            print("BUTTON PRESSED...!")
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopped by the user...!")
finally:
    print("PROGRAMMED ENDDED ...!")
    GPIO.cleanup()
#-------------------------------------------------------#
