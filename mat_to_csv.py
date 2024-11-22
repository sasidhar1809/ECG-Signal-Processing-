import scipy.io
import pandas as pd
import numpy as np  # Import NumPy

# Correct file path
mat_file = "D:\sasi\Downloads\ECG Signal Processing MATLAB\ecgdemo_edited\ECG_DEMO\ecgdemodata1.mat"
mat = scipy.io.loadmat(mat_file)

# Filter out metadata keys
mat_data = {k: v for k, v in mat.items() if not k.startswith('_')}

# Parse arrays within arrays in the .mat file
data = {}
for k, v in mat_data.items():
    arr = v[0]
    for i, sub_arr in enumerate(arr):
        lst = []
        if isinstance(sub_arr, (np.ndarray, list)):  # Check if sub_arr is an array or list
            for sub_index in range(len(sub_arr)):
                try:
                    vals = sub_arr[sub_index][0][0] if isinstance(sub_arr[sub_index][0], np.ndarray) else sub_arr[sub_index][0]
                except (IndexError, TypeError):
                    vals = sub_arr[sub_index] if isinstance(sub_arr[sub_index], (int, float)) else None
                lst.append(vals)
        else:
            lst.append(sub_arr)  # If sub_arr is scalar, directly add it
        data[f'row_{i}'] = lst

# Define columns and create DataFrame
columns = ['case', 'run', 'VB', 'time', 'DOC', 'feed', 'material', 'smcAC', 'smcDC', 'vib_table', 'vib_spindle', 'AE_table', 'AE_spindle']

# Ensure uniform row lengths by padding lists with None if needed
max_len = len(columns)
for key, values in data.items():
    if len(values) < max_len:
        data[key] = values + [None] * (max_len - len(values))

# Create the DataFrame
data_file = pd.DataFrame.from_dict(data, orient='index', columns=columns)

# Save to CSV
output_file = "D:/sasi/Downloads/mill1.csv"
data_file.to_csv(output_file, index=False)
print("Data successfully saved to", output_file)
