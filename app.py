import os

from flask import Flask, render_template
from flask import request
from packetAnalyzerSSL import *

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/operation_result", methods=['POST'])
def operation_result():
    val = request.form['the-message']
    msg = getCert(val)
    key1 = msg[1]
    key2 = msg[2]
    key3 = msg[3]
    return render_template('index.html', calculation_success=True, result=msg, result_1=key1, result_2=key2, result_3=key3)


if __name__ == '__main__':
    app.run()
