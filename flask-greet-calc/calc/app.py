# Put your app in here.
"""Basic math operations."""

from flask import Flask, request
from operations import *

app = Flask(__name__)


@app.route("/add")
def add_operation():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)

    return str(result)


@app.route("/sub")
def sub_operation():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)

    return str(result)


@app.route("/mult")
def mult_operation():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)

    return str(result)


@app.route("/div")
def div_operation():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)

    return str(result)
