from flask import Flask, jsonify, request
import requests 
import json


app = Flask(__name__)

@app.route('/oracle')
def ping():
    return jsonify('{"message": "ok"}')

    
if __name__ == '__main__':
    app.run(debug=True, port=5000)
