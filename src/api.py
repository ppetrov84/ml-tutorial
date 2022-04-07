from flask import Flask, request, Response
from flask_cors import CORS
import os
import pickle
import pandas as pd


app = Flask(__name__)

CORS(app)

training_data = pd.read_csv(os.path.join("data", "mpg.csv"))
file_to_open = open(os.path.join(
    "data", "models", "baummethoden_lr.pickle"), "rb")

trained_model = pickle.load(file_to_open)
file_to_open.close()


@ app.route("/", methods=["GET"])
def index():
    return {"Hello": "world"}


@ app.route("/hello_world", methods=["GET"])
def hello_world():
    return "<p>Hello world!</p>"


@ app.route("/training_data", methods=["GET"])
def get_training_data():
    return Response(training_data.to_json(), mimetype="application/json")


@ app.route("/predict", methods=["GET"])
def predict():
    zylinder = request.args.get("zylinder")
    ps = request.args.get("ps")
    gewicht = request.args.get("gewicht")
    beschleunigung = request.args.get("beschleunigung")
    baujahr = request.args.get("baujahr")

    if(zylinder and ps and gewicht and beschleunigung and baujahr):
        prediction = trained_model.predict(
            [[zylinder, ps, gewicht, beschleunigung, baujahr]])
        return{"result": prediction[0]}

    return Response("Daten fehlen")
