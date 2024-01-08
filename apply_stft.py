# import os
# import mne
# import matplotlib.pyplot as plt
# import numpy as np
# from scipy.signal import spectrogram

# # Define the path to the dataset
# data_path = "chb-mit-scalp-eeg-database-1.0.0/chb01/chb01_01.edf"

# # Create a directory to save the spectrogram images
# os.makedirs("spectrograms", exist_ok=True)

# # Define the window size and overlap
# window_size = 36000 # in seconds (adjust as needed)
# overlap = 20  # in seconds (adjust as needed)

# # Read the EDF file
# raw = mne.io.read_raw_edf(data_path, preload=True)

# fs = raw.info['sfreq']
# nperseg = int(window_size * fs)  # Number of samples in the window
# noverlap = int(overlap * fs)  # Overlap size

# # Calculate the spectrograms in a loop
# start_time = 0
# end_time = window_size

# while end_time <= raw.times[-1]:
#     # Calculate the spectrogram for the current window
#     data_window = raw.get_data(picks='T7-P7', start=int(start_time * fs), stop=int(end_time * fs))

#     f, t, Sxx = spectrogram(data_window[0], fs=fs, nperseg=nperseg, noverlap=noverlap, axis=0)
#     print(f"f= {f} , t = {t}, sxx = {Sxx}")
#     print(type(f), type(t), type(Sxx))
#     print(f.shape, t.shape, Sxx.shape)
#     # Spectrogram Plotting 
#     plt.figure()  # Create a new figure for each spectrogram
#     plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='auto', cmap='inferno', vmin=-30, vmax=30)
#     plt.ylabel('Frequency [Hz]')
#     plt.xlabel('Time [sec]')
#     plt.title('Spectrogram')
#     plt.colorbar(label='Intensity [dB]')
#     plt.tight_layout()
    
#     # Save the spectrogram as an image
#     output_filename = f'spectrograms/spectrogram_{os.path.basename(data_path)[:-4]}_{start_time}-{end_time}.png'
#     plt.savefig(output_filename)
#     plt.close()

#     # Update time intervals for the next window
#     start_time += (window_size - overlap)
#     end_time += (window_size - overlap)

# raw.close()  # Close the raw data



# for 1 spectogram

import os
import mne
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import spectrogram

# Define the path to the dataset
#data_path = "chb-mit-scalp-eeg-database-1.0.0/chb01/chb01_01.edf"

data_path = "chb-mit-scalp-eeg-database-1.0.0/chb01/chb01_02.edf"

# Create a directory to save the spectrogram images
os.makedirs("spectrograms", exist_ok=True)

# Read the EDF file
raw = mne.io.read_raw_edf(data_path, preload=True)

fs = raw.info['sfreq']
nperseg = int(10 * fs)  # Number of samples in the window (adjust as needed)
noverlap = int(1 * fs)  # Overlap size (adjust as needed)

# Calculate the spectrogram for the entire recording
f, t, Sxx = spectrogram(raw.get_data(picks='T7-P7')[0], fs=fs, nperseg=nperseg, noverlap=noverlap)

# Plot and save the spectrogram
plt.figure()
plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='auto', cmap='inferno')
plt.title(f'Spectrogram of chb01/01_01.edf')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')
plt.colorbar(label='dB')
output_filename = f'spectrograms/spectrogram_{os.path.basename(data_path)[:-4]}.png'
plt.savefig(output_filename)
plt.close()

raw.close()  # Close the raw data
