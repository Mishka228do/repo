import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]
GPIO.setup(leds, GPIO.OUT)

while True:
    for l in leds:
        GPIO.output(l, 1)
        time.sleep(0.1)
        GPIO.output(l, 0)


