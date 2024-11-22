# **ECG Signal Processing and Heart Rate Detection**

This project is a **Streamlit-based web application** designed for processing ECG signals, detecting R-peaks, and calculating heart rate. It also performs frequency-domain analysis and visualizations to help users understand ECG signal characteristics.

---

## **Features**
- **File Upload Support**: 
  - Upload ECG data in `.csv` or `.mat` formats.
- **Signal Filtering**:
  - Removes noise using a bandpass filter (0.5 Hz to 50 Hz).
- **Heart Rate Detection**:
  - Identifies R-peaks in the ECG signal to compute the average heart rate.
- **Noise Addition**:
  - Adds Gaussian noise to demonstrate signal processing techniques.
- **Interactive Visualizations**:
  - Time-domain plots of original, noisy, and filtered ECG signals.
  - R-peak detection visualizations.
  - RR interval plot (time between consecutive R-peaks).
  - Frequency-domain analysis using FFT.
- **Frequency Spectrum Analysis**:
  - Displays the frequency components of the ECG signal.

---

## **Demo**
Here's how the app looks in action:

- **Time-Domain Signal Visualization**
  - Original ECG signal with noise and filtering.
- **R-Peak Detection**
  - Filtered signal with detected R-peaks marked.
- **Frequency Spectrum**
  - Magnitude of the ECG signal across different frequencies.

---

## **Technologies Used**
- **Programming Language**: Python
- **Libraries**:
  - `streamlit`: For creating the web application interface.
  - `numpy`: For numerical computations.
  - `pandas`: For handling `.csv` files.
  - `scipy`: For signal processing (filters, FFT, and peak detection).
  - `matplotlib`: For visualizing ECG signals and results.
  - `scipy.io`: For reading `.mat` files.

---

## **Installation**

Follow these steps to set up the project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/ecg-signal-processing.git
   cd ecg-signal-processing
   ```

2. **Set up a Virtual Environment** *(Optional but recommended)*:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**:
   ```bash
   streamlit run app.py
   ```

5. **Open in Browser**: The app will open in your default browser. If not, go to the URL provided in the terminal, typically `http://localhost:8501`.

---

## **File Format Requirements**
- **CSV Files**:
  - The first column should contain ECG signal values.
- **MAT Files**:
  - Should have a variable named `ecg_signal`.

---

## **How to Use the Application**

1. **Upload File**:
   - Select an `.csv` or `.mat` file containing ECG data.
2. **Set Sampling Frequency**:
   - Input the sampling frequency (in Hz) of the uploaded ECG signal.
3. **View Results**:
   - Visualize the original, noisy, and filtered ECG signals.
   - Observe detected R-peaks and calculated average heart rate.
   - Analyze RR intervals and the frequency spectrum of the signal.

---

## **Example Data**
If you do not have ECG data, you can use the following test datasets:

- `example.csv`: A sample ECG signal in `.csv` format.
- `example.mat`: A sample ECG signal in `.mat` format.

Add these files to the repository under a folder named `data/`.

---

## **Customization**
You can modify the following parameters in the code:
- **Bandpass Filter**:
  - Adjust `low_cutoff` and `high_cutoff` values for the bandpass filter.
- **R-Peak Detection**:
  - Modify `min_peak_height` and `min_peak_distance` for finer control over peak detection.
- **Noise Level**:
  - Change `noise_level` in the `add_noise` function.

---

## **Limitations**
- Assumes ECG data is clean and formatted correctly.
- May require parameter adjustments for non-standard datasets.
- Large datasets may slow down processing.

---

## **Future Enhancements**
- Add support for live streaming ECG data.
- Integrate additional signal processing methods like wavelet transform.
- Enable real-time heart rate monitoring.
- Support for more file formats like `.edf`.

---



### IT IS NOT AN MACHINE LEARNING MODEL ###
