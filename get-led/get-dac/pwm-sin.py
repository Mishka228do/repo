import time
import pwm_dac as pw
import signal_generator as sg

ampl = 3.1
sig_freq = 10
samp_freq = 1000

try:
    dac = pw.PWM_DAC(12, 500, 3.3, True)
    while True:
        sg.wait_for_sampling_period(samp_freq)
        t = time.perf_counter()
        vol = ampl * sg.det_sin_wave_amplitude(sig_freq, t)
        dac.outi(vol)

finally:
    dac.dinit()