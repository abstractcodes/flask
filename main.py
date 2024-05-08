# import dependency , jsonify to create json response
from flask import Flask, request, jsonify

# create application 

app = Flask(__name__)

# creating a root for the endpoint
@app.route("/")
def home():
    return "Home"

if __name__ == "__main__":
    app.run(debug = True)