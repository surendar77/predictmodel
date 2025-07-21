from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# Load trained model
model = joblib.load("model.pkl")

# Create FastAPI app
app = FastAPI(title="Student Result Prediction API")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Input schema
class StudentInput(BaseModel):
    Math: float
    Science: float
    English: float
@app.get("/")
def serve_home():
    return FileResponse("static/index.html")

@app.post("/predict")
def predict_result(student: StudentInput):
    data = pd.DataFrame([{
        "Math": student.Math,
        "Science": student.Science,
        "English": student.English
    }])
    prediction = model.predict(data)[0]
    result = "Pass" if prediction == 1 else "Fail"
    return {
        "prediction": result,
        "code": int(prediction)
    }
