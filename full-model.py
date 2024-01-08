import numpy as np
import mne
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from scipy.stats import skew, kurtosis

# Load EEG data from EDF files
def load_eeg_data(edf_file):
    raw = mne.io.read_raw_edf(edf_file, preload=True)
    data, times = raw[:, :]
    return data.T, raw.info['sfreq']

# Load seizure or normal information from CSV file
def load_data_info(csv_file):
    data_info = np.loadtxt(csv_file, dtype=str, delimiter=' ', skiprows=1)
    return data_info

def extract_features(segment, sfreq):
    features = []

    # Time-domain features
    mean_value = np.mean(segment, axis=0)
    std_dev = np.std(segment, axis=0)
    skewness = skew(segment, axis=0)
    kurt = kurtosis(segment, axis=0)

    # Additional features
    zero_crossings = np.sum(np.diff(np.sign(segment), axis=0) != 0, axis=0)
    crests = np.max(segment, axis=0)
    troughs = np.min(segment, axis=0)

    features.extend(mean_value)
    features.extend(std_dev)
    features.extend(skewness)
    features.extend(kurt)
    features.extend(zero_crossings)
    features.extend(crests)
    features.extend(troughs)

    return features
# Load seizure and normal data information
seizure_csv_file = 'seizure-info.csv'
normal_csv_file = 'normal-info.csv'

seizure_info = load_data_info(seizure_csv_file)
normal_info = load_data_info(normal_csv_file)

# Initialize empty lists for features and labels
X, y = [], []

# Process seizure data
for entry in seizure_info:
    edf_file, start, end = entry
    eeg_data, sfreq = load_eeg_data(edf_file)

    # Convert start and end times to indices
    start_idx = int(start)
    end_idx = int(end)

    # Extract features for each segment
    segment = eeg_data[start_idx:end_idx, :]
    features = extract_features(segment, sfreq)

    # Append features to X and label to y
    X.append(features)
    y.append(1)  # 1 indicates seizure

# Process normal data
for entry in normal_info:
    edf_file, start, end = entry
    eeg_data, sfreq = load_eeg_data(edf_file)

    # Convert start and end times to indices
    start_idx = int(start)
    end_idx = int(end)

    # Extract features for each segment
    segment = eeg_data[start_idx:end_idx, :]
    features = extract_features(segment, sfreq)

    # Append features to X and label to y
    X.append(features)
    y.append(0)  # 0 indicates normal

# Convert lists to arrays
X = np.array(X)
y = np.array(y)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Reshape X_train and X_test to be 3D
X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

# Larger LSTM model
larger_model = Sequential()
larger_model.add(LSTM(units=100, input_shape=(X_train.shape[1], X_train.shape[2]), return_sequences=True))
larger_model.add(LSTM(units=100, return_sequences=True))
larger_model.add(LSTM(units=100))
larger_model.add(Dense(units=50, activation='relu'))
larger_model.add(Dropout(0.2))  # Adding dropout for regularization
larger_model.add(Dense(units=1, activation='sigmoid'))

import numpy as np
import mne
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from scipy.stats import skew, kurtosis

# Load EEG data from EDF files
def load_eeg_data(edf_file):
    raw = mne.io.read_raw_edf(edf_file, preload=True)
    data, times = raw[:, :]
    return data.T, raw.info['sfreq']

# Load seizure or normal information from CSV file
def load_data_info(csv_file):
    data_info = np.loadtxt(csv_file, dtype=str, delimiter=' ', skiprows=1)
    return data_info

def extract_features(segment, sfreq):
    features = []

    # Time-domain features
    mean_value = np.mean(segment, axis=0)
    std_dev = np.std(segment, axis=0)
    skewness = skew(segment, axis=0)
    kurt = kurtosis(segment, axis=0)

    # Additional features
    zero_crossings = np.sum(np.diff(np.sign(segment), axis=0) != 0, axis=0)
    crests = np.max(segment, axis=0)
    troughs = np.min(segment, axis=0)

    features.extend(mean_value)
    features.extend(std_dev)
    features.extend(skewness)
    features.extend(kurt)
    features.extend(zero_crossings)
    features.extend(crests)
    features.extend(troughs)

    return features
# Load seizure and normal data information
seizure_csv_file = 'seizure-info.csv'
normal_csv_file = 'normal-info.csv'

seizure_info = load_data_info(seizure_csv_file)
normal_info = load_data_info(normal_csv_file)

# Initialize empty lists for features and labels
X, y = [], []

# Process seizure data
for entry in seizure_info:
    edf_file, start, end = entry
    eeg_data, sfreq = load_eeg_data(edf_file)

    # Convert start and end times to indices
    start_idx = int(start)
    end_idx = int(end)

    # Extract features for each segment
    segment = eeg_data[start_idx:end_idx, :]
    features = extract_features(segment, sfreq)

    # Append features to X and label to y
    X.append(features)
    y.append(1)  # 1 indicates seizure

# Process normal data
for entry in normal_info:
    edf_file, start, end = entry
    eeg_data, sfreq = load_eeg_data(edf_file)

    # Convert start and end times to indices
    start_idx = int(start)
    end_idx = int(end)

    # Extract features for each segment
    segment = eeg_data[start_idx:end_idx, :]
    features = extract_features(segment, sfreq)

    # Append features to X and label to y
    X.append(features)
    y.append(0)  # 0 indicates normal

# Convert lists to arrays
X = np.array(X)
y = np.array(y)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Reshape X_train and X_test to be 3D
X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
X_test = X_test.reshape((X_test.shape[0], X_test.shape[1], 1))

# Larger LSTM model
larger_model = Sequential()
larger_model.add(LSTM(units=100, input_shape=(X_train.shape[1], X_train.shape[2]), return_sequences=True))
larger_model.add(LSTM(units=100, return_sequences=True))
larger_model.add(LSTM(units=100))
larger_model.add(Dense(units=50, activation='relu'))
larger_model.add(Dropout(0.2))  # Adding dropout for regularization
larger_model.add(Dense(units=1, activation='sigmoid'))

larger_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Record accuracy history during training
history = larger_model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2)

# Save the trained model to an HDF5 file
model_save_path = 'path/to/save/your/model/model.h5'
larger_model.save(model_save_path)

# Evaluate the model
loss, accuracy = larger_model.evaluate(X_test, y_test)
print(f'Test Accuracy: {accuracy}')
import matplotlib.pyplot as plt

# Plot training and validation accuracy
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

import pandas as pd


print(X)
print(y)

edf_file_for_prediction = 'chb-mit-scalp-eeg-database-1.0.0\chb01\chb01_18.edf'

# Load EEG data from the specified EDF file
eeg_data_for_prediction, sfreq_for_prediction = load_eeg_data(edf_file_for_prediction)

# Specify the start and end seconds for the duration you want to predict on
start_seconds = 120
end_seconds = 150

# Load the EEG data for the specified duration
start_idx = int(start_seconds * sfreq_for_prediction)
end_idx = int(end_seconds * sfreq_for_prediction)
segment = eeg_data_for_prediction[start_idx:end_idx, :]

# Extract features for the segment
features = extract_features(segment, sfreq_for_prediction)

# Reshape features to match the input shape of the model
features = np.array([features])
features = features.reshape((features.shape[0], features.shape[1], 1))

# Make predictions on the reshaped features
predictions = larger_model.predict(features)


# Threshold the predictions to obtain binary labels
binary_predictions = (predictions > 0.5).astype(int)

# Convert binary labels to "normal" or "seizure"
label = "normal" if binary_predictions[0][0] == 0 else "seizure"

# Print or use the label as needed
print("Prediction:", label)


