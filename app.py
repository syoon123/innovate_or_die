from flask import Flask, render_template, request, url_for, session, redirect
import hashlib, sqlite3, json
from utils import auth

db = 'data/database.db'

app = Flask(__name__)
app.secret_key = "t\x1cJ\xce;\x88D\xdc\xa4^\xfa\x9f\xeb\xc5s\t\x02??\xc9X\xd1\xff\xe0\xd3\x7f\xc0\xe8\xfa\xc0c\xc3\xd7o\xc6\x9cV\x89\xb2\x97k\xac\x08\xa88\xdeS\x9b"

@app.route("/")
def home():
    if "user" not in session:
        return redirect(url_for("login"))
    else:
        status = ""
        if "status" in request.args:
            status = request.args.get("status")
        return render_template("index.html", status=status)

@app.route("/login/")
def login():
    return render_template("home.html", title="Login")

@app.route("/logout/")
def logout():
    if request.form["enter"] == "Logout":
        session.pop("user")
        print "this pussy DO pop for you"
    return redirect(url_for("login"))



if __name__ == "__main__":
    app.debug = True
    app.run()
    

