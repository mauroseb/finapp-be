# -*- coding: utf-8 -*-

import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "<h1>Welcome stranger.</h1>"

@app.route('/premarket')
def premarket():
    return 'Premarket outstanding variations are:'


@app.route('/price/<ticker>')
def price(ticker):
    price = 5678.1234
    return f"Price of symbol {ticker} is {price}"

@app.route('/intraday')
def intraday():
    return 'Intraday variation of symbol is Y'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
