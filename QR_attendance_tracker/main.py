from flask import Flask, render_template, request
from db import matchCreds

app = Flask(__name__)

@app.route("/")
def home():
    """ Serving Home Page"""

    return render_template('home.html')

@app.route("/qrscreen", methods=["POST"])
def qrscreen():
    """ Serving QR page for displaying QR"""
    userid = request.form["userID"]
    password = request.form["password"]
    print(userid, password)
    val = matchCreds(userid, password)
    print(val)
    if (val):
        return render_template('qrscreen.html', userID = userid)
    else:
        return "<h1>Invalid credentials</h1>"
# Main driver Function
if __name__ == "__main__":
    app.run(debug=True)
