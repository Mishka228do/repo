import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
leds = [24, 22, 23, 27, 17, 25, 12, 16]
GPIO.setup(leds, GPIO.OUT)

GPIO.setup(9, GPIO.IN)
GPIO.setup(10, GPIO.IN)

for le in leds:
    GPIO.output(le, 0)
count = 0
while True:
    if GPIO.input(9) > 0:
        count += 1
    if GPIO.input(10) > 0:
        count -= 1
    time.sleep(0.2)
    if count > 255 or count < 0:
        count = 0
    c1 = [int(h) for h in bin(count)[2:].zfill(8)]
    print(count, c1)
    GPIO.output(leds, c1)



