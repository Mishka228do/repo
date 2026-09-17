import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [24, 22, 23, 27, 17, 25, 12, 16]
GPIO.setup(leds, GPIO.OUT)

up = 9
down = 10
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)

for le in leds:
    GPIO.output(le, 0)
count = 0
while True:
    if GPIO.input(up) and GPIO.input(down):
        count = 255
    elif GPIO.input(up) and not GPIO.input(down):
        count += 1
        if count > 255 or count < 0:
            count = 0
    elif GPIO.input(down) and not GPIO.input(up):
        count -= 1
        if count > 255 or count < 0:
            count = 0
    print(count, [int(h) for h in bin(count)[2:].zfill(8)])
    GPIO.output(leds, [int(h) for h in bin(count)[2:].zfill(8)])
    time.sleep(0.05)
    GPIO.output(leds, 0)