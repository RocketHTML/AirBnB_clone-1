#!/usr/bin/python3
"""
    This is a script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage
import web_flask.shadowhtml as shadowhtml
import os


app = Flask(__name__)
app.url_map.strict_slashes = False
os.environ['HBNB_TYPE_STORAGE'] = 'file'

@app.route('/shadow/')
@app.route('/shadow/<command>')
def print_eyes(command=None):
    link = "https://github.com/GucciGerm/Anime-Animation/blob/master/blinking_made_easy.gif?raw=true"
    template = shadowhtml.html.format(shadowhtml.img.format(link))
    return template

@app.route('/')
def landing_page():
    return("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    return("HBNB")


@app.route('/c/<text>')
def c(text):
    return("C {}".format(text.replace('_', ' ')))


@app.route('/python/')
@app.route('/python/<text>')
def pyroute(text='is cool'):
    return("Python {}".format(text.replace('_', ' ')))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)