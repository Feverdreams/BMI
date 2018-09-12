from biosppy import storage
from biosppy.signals import emg
# load raw Emg signal
signal, mdata = storage.load_txt('./examples/emg.txt')
# process it and plot
out = emg.emg(signal=signal, sampling_rate=1000., show=True)

