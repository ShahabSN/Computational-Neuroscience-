import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat

data = loadmat('/Users/zsnd/Downloads/EEG_P2090.mat')

print(data.keys())

EEG = data['EEG_P2090_processed']

num_channels = EEG.shape[0]
num_samples = EEG.shape[1]
print(f"number of channels: {num_channels}")
print(f"number of samples: {num_samples}")

fs = 500  # Frequency Sampling Rate

time = np.arange(num_samples) / fs  # corrected time

ch_toplot = 2
plt.figure(figsize=(10, 5))
plt.plot(time, EEG[ch_toplot, :])
plt.title(f"EEG signal of channel {ch_toplot}")
plt.xlabel("Time(seconds)")
plt.ylabel("Amplitude")

num_rows = 5
num_cols = 6
plt.figure(figsize=(18, 12))

for channel in range(num_channels):
    ch_toplot = channel
    plt.subplot(num_rows, num_cols, ch_toplot + 1)
    plt.plot(time, EEG[ch_toplot, :])
    plt.title(f"EEG signal of channel {ch_toplot}")
    plt.xlabel("Time(seconds)")
    plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()

input_time = []


def get_input_time():
    for i in range(2):
        start_time = int(input("Enter the start time: "))
        end_time = int(input("Enter the end time: "))
        input_time.append({"start": start_time, "end": end_time})


get_input_time()

print(input_time)

for time_range in input_time:
    start_sample = int(time_range["start"] * fs)
    end_sample = int(time_range["end"] * fs)

    for channel in range(num_channels):
        plt.figure(figsize=(10, 5))
        plt.plot(time[start_sample:end_sample], EEG[channel, start_sample:end_sample])
        plt.title(f'EEG signal range {start_sample} to {end_sample} of channel {channel}')
        plt.xlabel('Time(s)')
        plt.ylabel('Channel')
        plt.show()