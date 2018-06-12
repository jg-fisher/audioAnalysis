import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile
import sys

if len(sys.argv) < 2:
    print('Pass name of .wav as command line arg')
    sys.exit()

sample_rate, samples = wavfile.read(sys.argv[1])
frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

plt.pcolormesh(times, frequencies, spectrogram)
plt.imshow(spectrogram)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.show()
