from typing import List

from fastapi import FastAPI

import pandas as pd

from data_model import DataModel
from prediction_model import PredictionModel


app = FastAPI()


@app.get("/")
def hello_world():
   return { "message": "Hello world" }

@app.post("/predict")
def make_predictions(X: List[DataModel]):
    print(X)
    df = pd.DataFrame([x.dict() for x in X])

    predicion_model = PredictionModel()
    results = predicion_model.make_predictions(df)
    return results.tolist()
