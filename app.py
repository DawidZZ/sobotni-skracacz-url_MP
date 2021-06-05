from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/add", methods=["POST"])
def add():
    # Zrób coś aby wygenerować skrócony URL i zapamiętaj adres !
    return redirect("/success")
