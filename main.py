from fastapi import FastAPI
from sentiment import predict_sentiment #example of model as python module 
from population import predict_population #example of model extracted from pickle

app = FastAPI()

@app.get("/")
def read_root():
    return ("Welcome to Prediction service")

@app.post("/predict/sentiment")
def predict_senti(text: str):
    return predict_sentiment(text)

@app.post("/predict/population")
def predict_pops(year: int):
    return predict_population(year)