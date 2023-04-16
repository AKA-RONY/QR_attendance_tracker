from flask import Flask, render_template, request
from db import matchCreds

app = Flask(__name__)


@app.route("/")
def home():
    """ Serving Home Page"""

    return render_template('home.html')


@app.route("/portal", methods=["POST"])
def portal():
    """ Serving QR page for displaying QR"""
    userid = request.form["userID"]
    password = request.form["password"]
    print(userid, password)
    val = matchCreds(userid, password)
    if (val == 0):
        return render_template('qrscreen.html', userID=userid)
    elif(val == 1):
        return render_template("teacherPortal.html")
    elif(val == 2):
        return render_template("admin.html")


# Main driver Function
if __name__ == "__main__":
    app.run(debug=True)
