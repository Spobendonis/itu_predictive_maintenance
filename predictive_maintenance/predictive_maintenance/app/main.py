from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import PlainTextResponse

from prometheus_client import Gauge, Summary, generate_latest
import random
import time
import requests

from predictive_maintenance.model.inference import Inference

app = FastAPI()
inference = Inference()

class Prediction(BaseModel):
    failure_prediction: float

metricsOutput = Gauge('device_health', 'device_health', ['id'])

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    i = 0
    while i < 1000 :
        inputDevice = requests.get("http://localhost:8000/get_record").json()
        pred = requests.post("http://localhost:8001/predict", json=inputDevice)
        metricsOutput.labels(id = f"{i}").set(pred.json()['failure_prediction'])
        i = i+1
    return generate_latest(metricsOutput)

@app.post("/predict/", response_model=Prediction)
def predict(data: dict):
    prediction = inference.predict(data)
    return Prediction(failure_prediction=prediction)
