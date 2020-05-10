# -*- coding: utf-8 -*-

import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "HELLO WORLD"

@app.route('/premarket')
def premarket():
    return 'Premarket outstanding variations are:'


@app.route('/price')
def price():
    return 'Price of symbol is X'

@app.route('/intraday')
def intraday():
    return 'Intraday variation of symbol is Y'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
