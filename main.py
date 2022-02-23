# from flask import Flask
# app = Flask(__name__)
# from src.utils.myfunc import my_function

import flask
from flask import jsonify, request


from src.utils.sample_one import sample_one


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"



app.run()
