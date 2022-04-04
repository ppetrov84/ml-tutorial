from flask import Flask
from flask_cors import CORS
import os
import pandas as pd
from werkzeug import Response


app = Flask(__name__)

CORS(app)

training_data = pd.read_csv(os.path.join("data", "mpg.csv"))


@app.route("/", methods=["GET"])
def index():
    return {"Hello": "world"}


@app.route("/hello_world", methods=["GET"])
def hello_world():
    return "<p>Hello world!</p>"


@app.route("/training_data", methods=["GET"])
def get_training_data():
    return Response(training_data.to_json(), mimetype="application/json")
