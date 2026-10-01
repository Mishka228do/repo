import numpy as np
import time

def det_sin_wave_amplitude(freq, time):
    return (np.sin(np.pi * 2 * freq * time) + 1) / 2

def wait_for_sampling_period(sampling_frequency):
    time.sleep(1 / sampling_frequency)