from flask import Flask, render_template, request, url_for, session, redirect
import hashlib, sqlite3, json, requests
from utils import auth, getlegislators

db = 'data/database.db'

app = Flask(__name__)
app.secret_key = "t\x1cJ\xce;\x88D\xdc\xa4^\xfa\x9f\xeb\xc5s\t\x02??\xc9X\xd1\xff\xe0\xd3\x7f\xc0\xe8\xfa\xc0c\xc3\xd7o\xc6\x9cV\x89\xb2\x97k\xac\x08\xa88\xdeS\x9b"


@app.route("/")
def home():
    if "user" not in session:
        pass
        return redirect(url_for("login"))
    else:
        status = ""
        if "status" in request.args:
            status = request.args.get("status")
        return render_template("index.html")

@app.route("/login/", methods=["GET","POST"])
def login():
    if "user" in session:
        return redirect(url_for("home"))
    if request.method == "GET":
        return render_template("login.html", status="lemow")
    if request.form["enter"] == "Register":
        register_message = auth.register(request.form["user"], request.form["pass"])
        return render_template("login.html", status = register_message)
    if request.form["enter"] == "Login":
        login_message = auth.checkLogin(request.form["user"], request.form["pass"])
        if (login_message == ""):
            session["user"] = request.form["user"]
            return redirect(url_for("home"))
    return render_template("login.html", status = login_message)
    
@app.route("/logout/")
def logout():
    session.pop("user")
    print "this pussy DO pop for you"
    return redirect(url_for("home"))

@app.route("/legislators/", methods=["GET"] )
def myLegislators():

    if request.args.get("state") == "-1":
        url = "http://ip-api.com/json"
        geo = requests.get(url)
        state = geo.json()["region"]
    else:
        state = request.args.get("state")
    
    housedict = getlegislators.getLegislators(state)["house"]
    senatedict = getlegislators.getLegislators(state)["senate"]
    return render_template("legislators.html", house = housedict, senate = senatedict, state_abbrev = state)

if __name__ == "__main__":
    app.debug = True
    app.run()
    

