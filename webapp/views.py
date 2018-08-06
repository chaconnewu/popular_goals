'''
View.py
'''

from flask import render_template
from webapp import app

@app.route("/")
def index():
    '''
    root handler
    '''
    python_data = {"some_list": [4, 5, 6], "nested_dict": {"foo": 7, "bar": "a string"}}
    return render_template("index.html", pydata=python_data)
