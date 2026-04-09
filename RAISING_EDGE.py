#RAISING EDGE
import RPi.GPIO as GPIO
import time
#------------------------------------------------------------#
BUTTON_PIN = 17
flag = 1
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#-------------------------------------------------------------#
try:
    while True:
        button = GPIO.input(BUTTON_PIN)
        
        if button == 1 and flag == 1:
            print("BUTTON PRESSED...!")
            flag = 0
        elif button == 0:
            flag = 1
        time.sleep(0.05)
except KeyboardInterrupt:
    print("stoped by the programmer...!")
finally:
    print("print program ended...!")
    GPIO.cleanup()
#------------------------------------------------------------#