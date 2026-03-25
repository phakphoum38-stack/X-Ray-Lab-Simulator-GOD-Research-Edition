from flask import Flask,request

app = Flask(__name__)

images = []

@app.route("/upload",methods=["POST"])
def upload():

    data = request.json

    images.append(data)

    return {"status":"stored"}

def start():

    app.run(port=104)
