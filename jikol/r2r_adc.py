import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def dinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def number_to_dac(self, number):
        c1 = [int(h) for h in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio, c1)
    
    def sequental_counting_adc(self):
        count = 0
        while True:
            count += 1
            if count > 255 or count < 0:
                return 255
            self.number_to_dac(count)
            time.sleep(self.compare_time)

            if GPIO.input(self.comp_gpio) == 1:
                return count - 1
    def v(self):
        return self.sequental_counting_adc() / 255 * self.dynamic_range
    
    def binpoisk(self):
        code = 0
        bit = 128
        while bit > 0:
            test = code | bit
            self.number_to_dac(test)
            time.sleep(self.compare_time)
            
            if GPIO.input(self.comp_gpio) == 0:
                code = test
            bit >>= 1
        return code
    
    def v1(self):
        return self.binpoisk() / 255 * self.dynamic_range

if __name__ == "__main__":
    try:
        dac = R2R_ADC(3.2) 
        while True:
            print(dac.v1()) #для задания 1 прописать тут v
    finally:
        dac.dinit()
