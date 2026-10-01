import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
leds = [16, 20, 21, 25, 26, 17, 27, 22]
GPIO.setup(leds, GPIO.OUT)
diap = 3.3

def v(vol):
    if 0 <= vol <= diap:
        return int(vol/diap * 255)
    else:
        print('ОШИБКА')
        return 0
def outi(a):
    x = [int(i) for i in bin(a)[2:].zfill(8)]
    print(x)
    GPIO.output(leds, x)
try:
    while True:
        print('vvedite napryazhenie')
        vol = float(input())
        vol1 = v(vol)
        outi(vol1)
finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()
