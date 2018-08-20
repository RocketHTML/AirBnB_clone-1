#!/usr/bin/python3
"""
    This is a script that starts a Flask web application
"""

from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


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
