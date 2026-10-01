
import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, pwmpin, pwm,  diap, verbose = False):
        self.gpio_bits = pwmpin
        self.pwm1 = pwm
        self.diap= diap
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT)
        self.pwm = GPIO.PWM(self.gpio_bits, self.pwm1)
        duty = 0.0
        self.pwm.start(duty)

    def dinit(self):
        self.pwm.ChangeDutyCycle(0)

    '''def v(self, vol):
        if 0 <= vol <= self.diap:
            return int(vol/self.diap * 255)
        else:
            print('ОШИБКА')
            return 0'''
    def outi(self, a):
        self.pwm.ChangeDutyCycle(a/self.diap * 100)
if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.3, True)

        while True:
            print('vvedite napryazhenie')
            vol = float(input())
            if 0 <= vol <= 3.3:
                dac.outi(vol)
            else:
                print('OSHIBKA!!!!!!')

    finally:
        dac.dinit()