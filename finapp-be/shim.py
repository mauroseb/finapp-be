# -*- coding: utf-8 -*-

import os
import socket
import time
import json
from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

def check_backend():
    return 'success'

@app.route("/")
def main():
    return "<h1>Welcome stranger.</h1>"

@app.route('/api/v1/premarket')
def premarket():
    return 'Premarket outstanding variations are:'


@app.route('/api/v1/price/<ticker>')
def price(ticker):
    price = 5678.1234
    return f"Price of symbol {ticker} is {price}"

@app.route('/api/v1/intraday')
def intraday():
    return 'Intraday variation of symbol is Y'

@app.route('/api/v1/healthcheck')
def healthcheck():
    """Healthcheck endpoint"""

    status = check_backend()
    status_code = 200 if status == 'success' else 500

    if 'Cache-Control' not in response.headers:
        response.headers['Cache-Control'] = 'no-store'

    data = {
        'hostname': socket.gethostname(),
        'status': status,
        'timestamp': time.time(),
        'results': results,
    }

    return Response(json.dumps(data), status=status_code, mimetype='application/json')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

