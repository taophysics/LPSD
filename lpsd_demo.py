# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from lpsd import lpsd
from scipy import signal

N = int(1e5)  # Number of data points in the timeseries
fs = 2.  # sampling rate
fmin = float(fs) / N  # lowest frequency of interest
fmax = float(fs) / 2.  # highest frequency of interest
Jdes = 1000  # desired number of points in the spectrum
Kdes = 100  # desired number of averages
Kmin = 2  # minimum number of averages
xi = 0.5  # fractional overlap
x = np.random.normal(size=N)
X, f, C= lpsd(x, signal.hann, fmin, fmax, Jdes, Kdes, Kmin, fs, xi)

# Compare to Pwelch
nfft = np.ceil(fs / float(fmin))
f_Pwelch,  Pxx=signal.welch(x, fs, nperseg=N)
plt.loglog(f_Pwelch, Pxx)
plt.loglog(f, X*C['PSD'])
plt.show()
