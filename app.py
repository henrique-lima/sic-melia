from flask import Flask
from flask import render_template
from predict_utils import Predict_Utils
import json
import jsonpickle
from utils import Utils

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/events")
def events():
	predict_utils = Predict_Utils()
	events = predict_utils.get_concerts('10km@41.3948976,2.0787279,12', '2019-07-17T00:00:00+0200', '2019-07-20T00:00:00+0200')
	utils = Utils()
	return utils.serialize_list(events)

if __name__ == '__main__':
    app.run(debug=True)