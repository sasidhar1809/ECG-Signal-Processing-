import streamlit as st
import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt
import pandas as pd
from scipy.io import loadmat

# Function to process ECG data
def process_ecg_data(ecg_signal, fs):
    # Bandpass filter
    low_cutoff = 0.5
    high_cutoff = 50
    nyquist = 0.5 * fs
    low = low_cutoff / nyquist
    high = high_cutoff / nyquist
    b, a = signal.butter(2, [low, high], btype='band')
    filtered_signal = signal.filtfilt(b, a, ecg_signal)

    # R-peak detection
    min_peak_height = 0.5
    min_peak_distance = int(0.6 * fs)
    peaks, _ = signal.find_peaks(filtered_signal, height=min_peak_height, distance=min_peak_distance)

    # Calculate heart rate (bpm)
    rr_intervals = np.diff(peaks) / fs  # RR intervals in seconds
    heart_rate = 60 / rr_intervals  # Heart rate in bpm
    avg_heart_rate = np.mean(heart_rate)  # Average heart rate

    return filtered_signal, peaks, avg_heart_rate, rr_intervals

# Function for Frequency-Domain Analysis
def frequency_domain_analysis(ecg_signal, fs):
    # Apply FFT
    n = len(ecg_signal)
    fft_signal = np.fft.fft(ecg_signal)
    fft_freqs = np.fft.fftfreq(n, 1/fs)
    
    # Get the positive frequencies
    positive_freqs = fft_freqs[:n//2]
    positive_fft = np.abs(fft_signal[:n//2])

    return positive_freqs, positive_fft

# Function to add noise to the ECG signal
def add_noise(ecg_signal, noise_type='gaussian', noise_level=0.1):
    np.random.seed(0)  # For reproducibility
    if noise_type == 'gaussian':
        noise = np.random.normal(0, noise_level, len(ecg_signal))
    elif noise_type == 'uniform':
        noise = np.random.uniform(-noise_level, noise_level, len(ecg_signal))
    noisy_signal = ecg_signal + noise
    return noisy_signal

# Title and file uploader in Streamlit
st.title("ECG Signal Processing and Heart Rate Detection")

uploaded_file = st.file_uploader("Upload an ECG data file (.csv or .mat)", type=["csv", "mat"])

if uploaded_file is not None:
    # Load ECG data
    if uploaded_file.name.endswith('.csv'):
        # Use pandas to handle possible headers and extract the first column as ECG data
        df = pd.read_csv(uploaded_file)
        ecg_signal = df.iloc[:, 0].values  # Extract the first column (adjust if needed)
    elif uploaded_file.name.endswith('.mat'):
        data = loadmat(uploaded_file)
        ecg_signal = data['ecg_signal'][0]  # Adjust based on your .mat file structure

    # Input for sampling frequency
    fs = st.number_input("Sampling Frequency (Hz)", min_value=100, max_value=1000, value=500, step=10)

    # Process ECG data
    filtered_signal, peaks, avg_heart_rate, rr_intervals = process_ecg_data(ecg_signal, fs)

    # Add noise to the ECG signal
    noisy_signal = add_noise(ecg_signal, noise_type='gaussian', noise_level=0.3)

    # Plot Original, Noisy, and Filtered Signal
    time = np.arange(len(ecg_signal)) / fs  # Time axis for plotting
    plt.figure(figsize=(10, 4))
    plt.plot(time, ecg_signal, label='Original ECG')
    plt.plot(time, noisy_signal, label='Noisy ECG', linestyle='--')
    plt.plot(time, filtered_signal, label='Filtered ECG', linewidth=2)
    plt.legend()
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('ECG Signal with Noise and Filtered Signal')
    st.pyplot(plt)  # Show the plot in Streamlit

    # Plot R-peaks on the Filtered Signal
    plt.figure(figsize=(10, 4))
    plt.plot(time, filtered_signal, label='Filtered ECG')
    plt.plot(time[peaks], filtered_signal[peaks], 'ro', label='R-peaks')
    plt.legend()
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.title('R-peak Detection')
    st.pyplot(plt)

    # Display Average Heart Rate
    st.write(f'**Average Heart Rate:** {avg_heart_rate:.2f} bpm')

    # Optionally, plot RR intervals (time between R-peaks) if needed
    st.write("**RR Intervals (seconds):**")
    st.write(rr_intervals)
    
    # If you'd like to plot RR intervals as a graph:
    plt.figure(figsize=(10, 4))
    plt.plot(rr_intervals, label='RR Intervals')
    plt.xlabel('Beat Number')
    plt.ylabel('RR Interval (s)')
    plt.title('RR Intervals')
    st.pyplot(plt)
    
    # Frequency-Domain Analysis (FFT)
    positive_freqs, positive_fft = frequency_domain_analysis(filtered_signal, fs)

    # Plot Frequency Spectrum
    plt.figure(figsize=(10, 4))
    plt.plot(positive_freqs, positive_fft)
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude')
    plt.title('Frequency Spectrum of the ECG Signal')
    st.pyplot(plt)  # Show the frequency spectrum plot
