# pyrefly: ignore [missing-import]
import streamlit as st
import pickle
import pandas as pd


model = pickle.load(
    open("productivity_model.pkl", "rb")
)


st.title("🎓 Student Productivity Coach")


study = st.number_input(
    "Study Hours Per Day"
)

sleep = st.number_input(
    "Sleep Hours Per Night"
)

screen = st.number_input(
    "Screen Time Hours"
)

motivation = st.slider(
    "Motivation Level",
    1,
    10
)

assignments = st.number_input(
    "Assignments Completed"
)

attendance = st.number_input(
    "Attendance Percentage",
    min_value=0.0,
    max_value=100.0,
    value=80.0
)

participation = st.number_input(
    "Class Participation Score",
    min_value=0,
    max_value=100,
    value=50
)

gpa = st.number_input(
    "Previous Semester GPA",
    min_value=0.0,
    max_value=10.0,
    value=3.0
)

if st.button("Predict"):

    input_data = pd.DataFrame({

        "Study_Hours_Per_Day":[study],
        "Sleep_Hours_Per_Night":[sleep],
        "Screen_Time_Hours":[screen],
        "Motivation_Level":[motivation],
        "Assignments_Completed":[assignments],
        "Attendance_Percentage":[attendance],
        "Class_Participation_Score":[participation],
        "Previous_Semester_GPA":[gpa]

    })


    prediction = model.predict(
        input_data
    )


    st.success(
        f"Productivity Score: {prediction[0]:.2f}"
    )