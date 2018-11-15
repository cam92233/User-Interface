from flask import Flask, render_template, request, make_response
application = Flask(__name__)
import os

@application.route("/")
def hello():
    return make_response("<h1 style='color:blue'>Hello There!</h1>")

if __name__ == "__main__":
    application.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))