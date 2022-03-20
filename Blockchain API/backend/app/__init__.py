from flask import Flask

app = Flask(__name__)

@app.route("/")
def default():
    return "WELCOME TO THE BLOCKCHAIN"

app.run(port=5000)