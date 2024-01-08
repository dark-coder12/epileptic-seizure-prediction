import os
import mne
import matplotlib.pyplot as plt

# Define the path to the dataset
data_path = "chb-mit-scalp-eeg-database-1.0.0/chb01"

# List all the .edf files in the "chb01" directory
edf_files = [f for f in os.listdir(data_path) if f.endswith('.edf')]

# Create a list to store the loaded EEG data
raw_list = []

# Load each .edf file and append it to the raw_list
for edf_file in edf_files:
    edf_file_path = os.path.join(data_path, edf_file)
    raw = mne.io.read_raw_edf(edf_file_path, preload=True)
    raw_list.append(raw)

# Plot the EEG data from each file
for i, raw in enumerate(raw_list):
    plt.figure(figsize=(10, 5))
    raw.plot(n_channels=20, duration=10, title=f"EEG Data from {edf_files[i]}")
    plt.show()
