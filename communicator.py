import requests
import json
from time import sleep


class Communicator(object):

    @staticmethod
    def send_recieve(to_send):
        post_request = requests.post(
            "http://127.0.0.1:5000/getquote/", json=to_send
        )

        return post_request.json()["response"]

    @staticmethod
    def read_last():
        post_request = requests.get("http://127.0.0.1:5000/last/")

        # fetch post-response as json and print to terminal
        response = post_request.json()
        original_entry = response["entry_string"]
        processed_entry = response["processed_entry"]
        print(f"{original_entry} -> {processed_entry}")
