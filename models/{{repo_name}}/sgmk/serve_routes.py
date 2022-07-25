import os
import sys; sys.path.append(os.path.abspath(os.path.join(__file__, '..', '..')))
from markupsafe import escape
from flask import Flask
from flask import request, make_response
from sgmk.decorators import endpoint
from sgmk.decorators import model_load
import importlib
importlib.import_module('app')

app = Flask(__name__)

model_save_path = os.path.abspath(os.path.join(__file__, "../../model"))

# Load the model outside endpoint_function and on the server startup
m = model_load.load_function()
load_result = m._function(model_save_path=model_save_path)


@app.route("/ping", methods=["GET"])
def ping():
    message = {"status": "OK"}
    response = make_response(message, 200)
    response.mimetype = 'application/json'
    return response


@app.route("/invocations", methods=["POST"])
def invoc():
    e = endpoint.endpoint_function()
    message = e._function(json_dict=request.json, model=load_result)
    response = make_response(message, 200)
    response.mimetype = 'application/json'
    return response


def main():
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8080)


main()
