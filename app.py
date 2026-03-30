from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("ust_model.pkl")

@app.post("/predict")
def predict(data: dict):

    features = np.array([[
        data["latitude"],
        data["longitude"],
        data["crime"],
        data["lighting"],
        data["crowd"],
        data["hour"]
    ]])

    prediction = model.predict(features)

    classes = ["Safe", "Moderate", "High Risk"]

    return {"risk_class": classes[int(prediction[0])]}
