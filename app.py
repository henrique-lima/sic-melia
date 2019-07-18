from flask import Flask
from flask import render_template
from predict_utils import Predict_Utils
import json
import jsonpickle
from utils import Utils

app = Flask(__name__)

@app.route("/party")
def index_party():
	return render_template("index_party.html")

@app.route("/relax")
def index_food():
	return render_template("index_relax.html")

@app.route("/social")
def index_social():
	return render_template("index_social.html")

@app.route("/api/events")
def events():
	predict_utils = Predict_Utils()
	events = predict_utils.get_concerts('10km@41.3948976,2.0787279,12', '2019-07-19T00:00:00+0200', '2019-07-21T00:00:00+0200')
	utils = Utils()
	return utils.serialize_list(events)

if __name__ == '__main__':
    app.run(debug=True)