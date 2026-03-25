from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():

    return "X-Ray Lab Simulator"

def run():

    app.run(port=8080)
