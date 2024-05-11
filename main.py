from fastapi import FastAPI
from sentiment import predict_sentiment

app = FastAPI()

@app.get("/")
def read_root():
    return ("Welcome to Prediction service")

@app.post("/predict/sentiment")
def predict_senti(text: str):
    return predict_sentiment(text)