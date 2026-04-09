#PULL_DOWN_WITH_LEVEL_TRIGGERING

import RPi.GPIO as GPIO
import time
#-----------------------------------------------------------#
BUTTON_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setwarnings(False)
#-----------------------------------------------------------#
try:
    while True:
        state = GPIO.input(BUTTON_PIN)
        if state == 0:
            print("BUTTON NOT PRESSED..!")
        else:
            print("BUTTON PRESSED..!")
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopped by the user...!")
finally:
    print("Program ended ...!")
    GPIO.cleanup()
#----------------------------------------------------------#