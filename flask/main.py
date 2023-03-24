from flask import Flask, request

import pandas as pd

from prediction_model import PredictionModel


app = Flask(__name__)


@app.route("/")
def hello_world():
    return { "message": "Hello world" }

@app.route("/predict", methods=["POST"])
def make_predictions():
    X = request.json
    df = pd.DataFrame(X)
    predicion_model = PredictionModel()
    results = predicion_model.make_predictions(df)
    return results.tolist()