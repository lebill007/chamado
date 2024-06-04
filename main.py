from flask import Flask

app = Flask(__name__)
@app.route("/")
def curso():
    return "ola"

if __name__== "__maina__":
    app.run(debug=True)   