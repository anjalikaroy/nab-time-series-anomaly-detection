# Understanding the Data
# Import Libraries
import os
import pandas as pd

# Define Data Path
DATA_PATH = "data/raw/realKnownCause/realKnownCause"

# Step 3: List Files
files = os.listdir(DATA_PATH)
print(files)

# Step 4: Select a File
file_name = files[0]
print(file_name)

# Step 5: Create Full Path
file_path = os.path.join(DATA_PATH, file_name)
print(file_path)

# Step 6: Load CSV
time_series_data = pd.read_csv(file_path)

# Step 7: Initial Exploration
print(time_series_data.head())
print(time_series_data.shape)
print(time_series_data.info())
print(time_series_data.isnull().sum())
# print(type("data/raw/realKnownCause/realKnownCause/ambient_temperature_system_failure.csv"))

# Step 8: Convert Timestamp
time_series_data["timestamp"] = pd.to_datetime(time_series_data["timestamp"])
print(time_series_data.info())
