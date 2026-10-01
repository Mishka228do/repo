import signal_generator as sg
import time
import RPi.GPIO as GPIO

ampl = 3.2
sig_freq = 10
samp_freq = 1000

try:
    class R2R_DAC:
        def __init__(self, leds, diap, verbose = False):
            self.gpio_bits = leds
            self.diap= diap
            self.verbose = verbose

            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

        def dinit(self):
            GPIO.output(self.gpio_bits, 0)
            GPIO.cleanup()

        def v(self, vol):
            if 0 <= vol <= self.diap:
                return int(vol/self.diap * 255)
            else:
                print('ОШИБКА')
                return 0
        def outi(self, a):
            x = [int(i) for i in bin(a)[2:].zfill(8)]
            print(x)
            GPIO.output(self.gpio_bits, x)
    dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.3, True)
    while True:
        sg.wait_for_sampling_period(samp_freq)
        t = time.perf_counter()
        vol = ampl * sg.det_sin_wave_amplitude(sig_freq, t)
        vol1 = dac.v(vol)
        dac.outi(vol1)
finally:
    dac.dinit()