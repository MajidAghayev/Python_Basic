from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    if username == "admin" and password == "password":
        return redirect("/home")
    else:
        return redirect("/")

@app.route("/home")
def home():
    return "Welcome, Admin!"

if __name__ == "__main__":
    app.run()
