from itertools import islice

from flask import Flask, jsonify, make_response


app = Flask(__name__)


def fib():
    """
    Generates the fibonacci sequence of number starting from 0, 1. This
    generator will produce endless sequence of the numbers
    :returns: iterator
    """
    a, b = 0, 1

    while True:
        yield a
        a, b = b, a + b


def _validate_num(num):
    """
    Validation of the number is done in this function. Currently it only
    checks if the number is non 0, but for extensibility purposes we could
    add more validation checks in future
    :param num: integer
    :raises: ValueError
    """
    if num < 0:
        raise ValueError(
            "Number should be greater than 0")


@app.route("/fib/<int:num>", methods=["GET"])
def get_fib_sequence(num):
    """
    Flask provide the validation of the integer number and it will not accept
    the negative number in the url parameter. So the validation is currently
    redundant, but if we add more validations to the number then we could use
    this
    """
    try:
        _validate_num(num)
    except ValueError as e:
        error = {"error": str(e)}
        return make_response(jsonify(error), 400)
    seq = list(islice(fib(), num))
    return jsonify(seq)
