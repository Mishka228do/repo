import RPi.GPIO as GPIO
import time
from matplotlib import pyplot as plt


def plot_voltage_vs_time(time, voltage):
    plt.figure(figsize=(10, 6))
    plt.plot(time, voltage)
    plt.title("Зависимость ацп от входа цап")
    plt.grid(True)
    plt.show()

def plot_sampling_period(time):
    sp = []
    for i in range (len(time) - 1):
        sp.append(time[i + 1] - time[i])
    plt.figure(figsize=(10, 6))
    plt.hist(sp)
    plt.title("Зависимость ацп от входа цап1")
    plt.grid(True)
    plt.show()
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
voltageval = []
timeval = []
duration = 3.0
if __name__ == "__main__":
    try:
        dac = R2R_ADC(3.2) 
        start = time.perf_counter()
        while time.perf_counter() - start < duration:
            voltageval.append(dac.v1())
            timeval.append(time.perf_counter() - start)
        plot_voltage_vs_time(timeval, voltageval)
        plot_sampling_period(timeval)
        print(timeval)
    finally:
        dac.dinit()
