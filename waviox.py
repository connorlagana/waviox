import numpy as np
import wavio

rate = 22050  # samples per second
T = 10         # sample duration (seconds)
f = 900.0     # sound frequency (Hz)
t = np.linspace(0, T, T*rate, endpoint=False)
x = np.sin(2*np.pi * f * t)
wavio.write("sine24.wav", x, rate, sampwidth=3)
