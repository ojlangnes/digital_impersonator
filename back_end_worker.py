from flask import Flask, request
from flask_restful import Resource, Api
import requests
from random import randrange
import json
from back_end_processor import Quote
from time import sleep


app = Flask(__name__)
api = Api(app)


def return_to_front_end(to_send):
    requests.post("http://127.0.0.1:5000/recieve/", json=to_send)


def ask_processing(to_process):
    """ changes capitalization of letters at random """
    to_output = ""

    for letter in to_process["entry_string"]:
        if randrange(0, 2) is 1:
            to_output += letter.capitalize()
        else:
            to_output += letter

    # update dict with processed entry
    to_process.update({"processed_entry": to_output})

    return to_process


class Index(Resource):

    def get(self):
        return "IT WIRKLS"


class Processor(Resource):

    def post(self):
        user_input = request.get_json()
        response = Quote.quote(user_input["user_input"])
        response = {"response": response}

        return_to_front_end(response)


api.add_resource(Index, "/")
api.add_resource(Processor, "/processor/")

if __name__ == "__main__":
    app.run(port=5001, threaded=True, debug=True)
