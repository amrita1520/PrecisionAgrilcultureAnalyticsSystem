from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib
from datetime import datetime
app = FastAPI(title="predictionMLService", description="A simple FastAPI service for ML predictions.")
# ✅ Add CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows requests from any origin (change to specific domain if needed)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)
# Connect to MongoDB (default localhost:27017)
client = MongoClient("mongodb://localhost:27017/")
# Select Database & Collection
db = client["test"]  # Database
collection = db["student"]  # Collection
model = joblib.load(r"C:\Users\Arghya\PrecisionAgricultureAnalyticsSystem\iotdatagenerator\predictionMLService\linear_regression_model.pkl")

def predictdata(input_data):
    input_df = pd.DataFrame([{
        "sensor_id": input_data.sensor_id,
        "areagrid": input_data.areagrid,
        "droughtalert": input_data.droughtalert,
        "humidity": input_data.humidity,
        "temperature": input_data.temperature
    }])
    transformed_input = model.named_steps["preprocessor"].transform(input_df)

    prediction = model.named_steps["regressor"].predict(transformed_input)[0]
    # Prepare document for MongoDB
    prediction_document = {
        "sensor_id": input_data.sensor_id,
        "areagrid": input_data.areagrid,
        "droughtalert": input_data.droughtalert,
        "humidity": input_data.humidity,
        "temperature": input_data.temperature,
        "predicted_energy_usage": float(prediction),
        "timestamp": datetime.utcnow()
    }

    # Insert into MongoDB
    print(collection)
    collection.insert_one(prediction_document)

    return prediction  # Return as JSON

class PredictionInput(BaseModel):
    sensor_id: str
    areagrid: str
    droughtalert: float
    humidity: float
    temperature: float

class PredictionOutput(BaseModel):
    energy_usage: float

@app.post("/predict", response_model=PredictionOutput)
def predict(input_data: PredictionInput):
    energy_usage = predictdata(input_data)
    return PredictionOutput(energy_usage=energy_usage)

@app.get("/")
def read_root():
    return {"message": "Welcome to predictionMLService"}