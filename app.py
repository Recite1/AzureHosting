from flask import Flask, request, jsonify, abort, make_response
from dotenv import load_dotenv
import os

app = Flask(__name__)

database = os.getenv('DATABASE')

@app.route('/')
def index():
    return f'{{"message" : "Server is running"}}'
    
@app.route('/test')
def test():
    return f'{{"message" : {database}}}'


if __name__ == '__main__':
    app.run()
