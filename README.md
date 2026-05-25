# LINEAR_REGRESSION

A machine learning project that predicts student performance using a Linear Regression model. This repository contains the dataset, trained model, Streamlit application, and required dependencies for running the project.

## Overview

This project demonstrates a simple end-to-end machine learning workflow using Linear Regression. It takes student-related input data, processes it through a trained model, and returns a predicted performance output through a Streamlit web interface.

## Repository Structure

```bash
LINEAR_REGRESSION/
├── README.md
├── Student_Performance.csv
├── app.py
├── linear_regression_model.pkl
└── requirements.txt
```

## Files Included

- `Student_Performance.csv` - Dataset used for training and evaluation.
- `app.py` - Streamlit app used to collect input and display predictions.
- `linear_regression_model.pkl` - Pretrained Linear Regression model.
- `requirements.txt` - Required Python libraries for this project.
- `README.md` - Documentation for the repository.

## Features

- Predicts student performance using Linear Regression
- Interactive web app built with Streamlit
- Pretrained model included for direct use
- Clean and simple beginner-friendly project structure

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Pickle

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/RITHESH218/LINEAR_REGRESSION.git
   ```

2. Navigate to the project directory:
   ```bash
   cd LINEAR_REGRESSION
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Run the Streamlit app using:

```bash
streamlit run app.py
```

Then open the local URL displayed in the terminal to access the application in your browser.

## How It Works

1. The application loads the trained linear regression model.
2. The user provides input values in the Streamlit interface.
3. The model predicts the output based on the entered values.
4. The result is displayed on the screen.

## Learning Goals

This project is useful for understanding:
- Linear Regression basics
- Model saving and loading using pickle
- Streamlit deployment for machine learning apps
- Organizing an ML project repository

## Future Enhancements

- Add model evaluation metrics such as MAE, MSE, and R² score
- Add 
