"""Streamlit app to predict student performance using a saved linear regression model."""
import joblib
import numpy as np
import streamlit as st


MODEL_PATH = "linear_regression_model.pkl"


@st.cache_resource
def load_model():
	return joblib.load(MODEL_PATH)


def predict_performance(model, hours_studied, previous_scores, extracurricular, sleep_hours, question_papers):
    features = np.array(
        [[hours_studied, previous_scores, extracurricular, sleep_hours, question_papers]],
        dtype=float,
    )
    prediction = model.predict(features)
    return float(prediction[0])


st.set_page_config(page_title="Student Performance Predictor", layout="centered")
st.title("Student Performance Predictor")
st.write("Enter the student details to predict the performance index.")

model = load_model()

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
	hours_studied = st.slider("Hours Studied", min_value=0, max_value=24, step=1)
with col2:
	previous_scores = st.slider("Previous Scores", min_value=0, max_value=100, step=1)
with col3:
	extracurricular_label = st.selectbox("Activities", ["No", "Yes"])
with col4:
	sleep_hours = st.slider("Sleep Hours", min_value=0, max_value=24, step=1)
with col5:
	question_papers = st.slider("Question Papers", min_value=0, max_value=100, step=1)

extracurricular = 1.0 if extracurricular_label == "Yes" else 0.0

if st.button("Predict Performance"):
    prediction = predict_performance(
        model,
        hours_studied,
        previous_scores,
        extracurricular,
        sleep_hours,
        question_papers,
    )
    st.success(f"Predicted Performance Index: {int(round(prediction))}")