from flask import Flask, request, jsonify, abort, make_response
from dotenv import load_dotenv
import os

app = Flask(__name__)



@app.route('/')
def index():
    return f'{{"message" : "Server is running"}}'


if __name__ == '__main__':
    app.run()