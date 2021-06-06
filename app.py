from flask import Flask, render_template, redirect, request
app = Flask(__name__)

url_list = []
id = 0
short_url = ""

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success")
def success():
    return render_template("success.html", short_url = short_url, id = id)

@app.route("/add", methods=["POST"])
def add():
    global id
    id += 1
    long_url = request.form.get('long-url')
    url_list.append({"url": long_url, "id": id})

    global short_url 
    short_url = f"http://127.0.0.1:5000/shortener/{id}"
    return redirect("/success")

@app.route("/shortener/<id>")
def findAdress(id):
    return redirect(url_list[int(id) - 1].get("url"))
    