from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    """ Serveing Home Page"""

    return render_template('home.html')

@app.route("/qrscreen", methods=["POST"])
def qrscreen():
    """ Serving QR page for displaying QR"""
    userid = request.form["userID"]
    password = request.form["password"]
    print(userid, password)
    
    return render_template('qrscreen.html')

# Main driver Function
if __name__ == "__main__":
    app.run(debug=True)
