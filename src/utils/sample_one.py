import os
import json
from flask import render_template

def showjson():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "static/data", "taiwan.json")
    data = json.load(open(json_url))
    return render_template('showjson.jade', data=data)