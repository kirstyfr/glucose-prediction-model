# Data Analysis and Model Development for Sensor Calibration

This project involves analyzing experimental data to develop a mathematical model that describes the relationship between glucose concentration and the electrical current response of a biosensor. The model will be used for routine quality control tests on newly manufactured biosensors.

## Project Overview
- **Objective**: Build a mathematical model to describe the sensor's electrical current response at varying glucose concentrations.
- **Key Steps**:
  1. Extract stable current-glucose pairs from the experimental data.
  2. Fit a mathematical model to the data.
  3. Evaluate the model's quality of fit.
  4. Visualize the results for better understanding and presentation.

## Data Format
The data is provided in a JSON file with the following structure:
- `'time_s'`: Time of measurement (seconds)
- `'current_nA'`: Electrical current response (nanoamperes)
- `'substrate_reference_mM'`: Glucose concentration (millimolar)

## Python Class Features:
- **Data Extraction**: Identifies and extracts stable current-glucose pairs.
- **Model Fitting**: Fits a mathematical model to the data (e.g., linear regression).
- **Model Evaluation**: Uses metrics like R² and MSE to assess the fit.
- **Visualization**: Plots the experimental data and the fitted model.

## Technologies Used:
- Python
- NumPy, Pandas for data handling
- Matplotlib for data visualization
- SciPy or scikit-learn for model fitting and evaluation