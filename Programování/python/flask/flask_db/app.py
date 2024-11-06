from flask import Flask, render_template, request, redirect, url_for,g
import sqlite3
app = Flask(__name__)

DATBASE = "instance/database.db"

def get_db():
    db = getattr(g, "_database", None)
    if db is None :
        db = g._database = sqlite3.connect(DATBASE)
    return db

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource("schema.sql", mode="r") as file:
            db.cursor().executescript(file.read())
        db.commit()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g,"_database", None)
    if db is not None:
        db.close()

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/bye")
def bye(): 
    return render_template("bye.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name")
        input_class = request.form.get("class")
        message = request.form.get("message")

        if name and message and input_class:
            return redirect(url_for("result", name=name, form_class=input_class, message=message))
    
    return render_template("form.html")

@app.route("/result")
def result():
    name = request.args.get("name", default="_____")
    input_class = request.args.get("form_class", default="_____")
    message = request.args.get("message", default="_____")
    return render_template("result.html", name=name, form_class=input_class, message=message)



if __name__ == "__main__":
    app.run(debug=True)
    init_db()
    app.run(debug= True)