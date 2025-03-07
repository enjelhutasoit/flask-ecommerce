from flask import Flask

app = Flask(__name__)

@app.route('/')


def hellow_world():
    return "<!DOCTYPE html><html lang='en'><head><title>PHP Test</title></head><body>Hello World!</body></html>"