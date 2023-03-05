from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import PlainTextResponse

from predictive_maintenance.model.inference import Inference

app = FastAPI()
inference = Inference()

class Prediction(BaseModel):
    failure_prediction: float

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    response = PlainTextResponse("hello guys")
    return response

@app.post("/predict/", response_model=Prediction)
def predict(data: dict):
    prediction = inference.predict(data)
    return Prediction(failure_prediction=prediction)
