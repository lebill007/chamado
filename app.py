from flask import Flask, render_template, request, redirect, jsonify
from flask_mysqldb import MySQL    
from flask_bcrypt import Bcrypt
from datetime import date


app = Flask (__name__)



@app.route("/")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
    