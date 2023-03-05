from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import PlainTextResponse

from prometheus_client import Gauge, Summary, generate_latest
import random
import time
import requests

app = FastAPI()

metricsOutput = Gauge('device_health', 'device_health', ['id'])

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    i = 0
    while i < 10 :
        inputDevice = requests.get("http://localhost:8000/get_record").json()
        pred = requests.post("http://localhost:8001/predict", json=inputDevice)
        metricsOutput.labels(id = f"{i}").set(pred.json()['failure_prediction'])
        i = i+1
    return PlainTextResponse(generate_latest(metricsOutput))