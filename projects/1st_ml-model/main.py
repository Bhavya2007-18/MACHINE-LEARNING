import pickle
import pandas as pd
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os

app = FastAPI()

# Load the model
model_path = os.path.join(os.path.dirname(__file__), "productivity_model.pkl")
model = pickle.load(open(model_path, "rb"))

# Define input schema
class StudentData(BaseModel):
    Study_Hours_Per_Day: float
    Sleep_Hours_Per_Night: float
    Screen_Time_Hours: float
    Motivation_Level: float
    Assignments_Completed: float
    Attendance_Percentage: float
    Class_Participation_Score: float
    Previous_Semester_GPA: float

@app.post("/predict")
def predict(data: StudentData):
    # Convert input to DataFrame matching model features
    input_data = pd.DataFrame([{
        "Study_Hours_Per_Day": data.Study_Hours_Per_Day,
        "Sleep_Hours_Per_Night": data.Sleep_Hours_Per_Night,
        "Screen_Time_Hours": data.Screen_Time_Hours,
        "Motivation_Level": data.Motivation_Level,
        "Assignments_Completed": data.Assignments_Completed,
        "Attendance_Percentage": data.Attendance_Percentage,
        "Class_Participation_Score": data.Class_Participation_Score,
        "Previous_Semester_GPA": data.Previous_Semester_GPA
    }])
    
    # Reorder columns to exactly match what the model expects
    if hasattr(model, "feature_names_in_"):
        input_data = input_data[model.feature_names_in_]
    
    # Make prediction
    prediction = model.predict(input_data)
    
    return {"prediction": float(prediction[0])}

@app.get("/", response_class=HTMLResponse)
def read_root():
    ui_path = os.path.join(os.path.dirname(__file__), "ui.html")
    with open(ui_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
