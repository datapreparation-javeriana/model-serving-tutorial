from flask import Flask, request, render_template

import pandas as pd

from prediction_model import PredictionModel


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def make_predictions():
    X = request.json
    print(X)
    df = pd.DataFrame(X)

    predicion_model = PredictionModel()
    results = predicion_model.make_predictions(df)
    
    return results.tolist()


if __name__ == "__main__":
    app.run(debug=True)