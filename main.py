from flask import Flask, render_template, request
import sqlite3
from joblib import load

app = Flask(__name__)
app.secret_key = "ygfdffsfi99"
database = "data1.db"

# Define the error handler route
@app.errorhandler(404)
def page_not_found(error):
    return render_template('index.html'), 404

@app.route("/")
@app.route("/index")
def index():
    con = sqlite3.connect(database)
    cur = con.cursor()
    cur.execute("select * from result")
    data = cur.fetchall()
    data1 = len(data)
    return render_template("index.html", data=data1)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        number = request.form["number"]
        email = request.form["email"]
        password = request.form["pass"]
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("INSERT INTO user (user_name, number, mail, password) VALUES (?, ?, ?, ?)",
                    (name, number, email, password))
        conn.commit()
        return render_template("final.html", result="**successfully your profile registered**")
    return render_template("index.html")

name1 = []

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        name1.append(name)
        password = request.form["pass"]
        conn = sqlite3.connect(database)
        cur = conn.cursor()
        cur.execute("select * from user where user_name=? and password=?", (name, password,))
        data = cur.fetchone()
        if data:
            return render_template("spam.html")
        else:
            return render_template('index.html', error_message='Password mismatch')
    return render_template("index.html")

@app.route("/spam", methods=["GET","POST"])
def spam():
    if request.method == "POST":
        comment = request.form["comment"]
        loaded_model, loaded_vect = load('ExtraTreesClassifier.pkl')
        new_comment = [comment]
        new_comment_transformed = loaded_vect.transform(new_comment).toarray()
        prediction = loaded_model.predict(new_comment_transformed)[0]
        accuracy = loaded_model.predict_proba(new_comment_transformed)[0][1] * 100  # Convert accuracy to percentage
        if prediction == 1:
            prediction = "spam"
            conn = sqlite3.connect(database)
            cur = conn.cursor()
            cur.execute("insert into result (user_name,comment,result)values(?,?,?)", (name1[-1], comment, prediction))
            conn.commit()
            return render_template("final.html", result="The comment is spam", accuracy=accuracy)
        else:
            return render_template("final.html", result="The comment is not spam")
    return render_template("spam.html")

@app.route("/admin", methods=["GET","POST"])
def admin():
    if request.method == "POST":
        a = "admin"
        b = "admin"
        user = request.form["name"]
        password = request.form["pass"]
        if user == a and password == b:
            conn = sqlite3.connect(database)
            cur = conn.cursor()
            cur.execute("select * from result")
            result = cur.fetchall()
            return render_template("result.html", result=result)
        else:
            return render_template('index.html', error_message='Password mismatch')
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False, port=560)
