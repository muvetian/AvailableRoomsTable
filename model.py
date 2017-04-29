from flask import Flask
from flask import Flask, render_template, redirect, url_for, request, send_file
from get_available_rooms import *
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("template.html",available_rooms = get_available_rooms("Chambers"))

if __name__ == "__main__":
    app.run()