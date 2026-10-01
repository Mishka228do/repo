import time
import mcp4725_driver as md
import signal_generator as sg

ampl = 4.1
sig_freq = 10
samp_freq = 1000

try:
    dac = md.MCP4725(5.0, True)
    while True:
        sg.wait_for_sampling_period(samp_freq)
        t = time.perf_counter()
        vol = ampl * sg.timevoltage(sig_freq, t)
        dac.set_voltage(vol)

finally:
    dac.dinit()