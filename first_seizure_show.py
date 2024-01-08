import os
import mne
import matplotlib.pyplot as plt
from datetime import datetime

# Define the path to the dataset
data_path = "chb-mit-scalp-eeg-database-1.0.0/chb01"

# Specify the name of the .edf file you want to load
edf_file_name = "chb01_03.edf"

# Create the full path to the specific .edf file
edf_file_path = os.path.join(data_path, edf_file_name)

# Load the EEG data from the specified .edf file
raw = mne.io.read_raw_edf(edf_file_path, preload=True)

# Define the start and end times you want to annotate
start_time_str = "00:13:43"
end_time_str = "00:14:43"

# Convert the start and end times to seconds
start_time = datetime.strptime(start_time_str, "%H:%M:%S")
end_time = datetime.strptime(end_time_str, "%H:%M:%S")

# Calculate the time range in seconds
start_time_seconds = start_time.hour * 3600 + start_time.minute * 60 + start_time.second
end_time_seconds = end_time.hour * 3600 + end_time.minute * 60 + end_time.second

# Create an Annotation for the specified time range
my_annot = mne.Annotations(
    onset=[start_time_seconds],
    duration=[end_time_seconds - start_time_seconds],
    description=["Annotated Segment"]
)

print(start_time_seconds, end_time_seconds)
# Add the annotation to the EEG data
raw.set_annotations(my_annot)

# Plot the entire EEG file
plt.figure(figsize=(10, 5))
raw.plot(n_channels=20, title=f"EEG Data from {edf_file_name}")
plt.show()