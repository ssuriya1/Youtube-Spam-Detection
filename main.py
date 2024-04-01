from flask import Flask, render_template, request
import sqlite3
from joblib import load
from fetch_comments import get_video_comments

app = Flask(__name__)
database = "database.db"

# Create tables if they don't exist
def create_tables():
    conn = sqlite3.connect(database)
    cur = conn.cursor()
    # Create user table
    cur.execute('''CREATE TABLE IF NOT EXISTS user (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_name TEXT NOT NULL,
                    number TEXT NOT NULL,
                    mail TEXT NOT NULL,
                    password TEXT NOT NULL
                )''')
    # Create result table
    cur.execute('''CREATE TABLE IF NOT EXISTS result (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_name TEXT NOT NULL,
                    comment TEXT NOT NULL,
                    result TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

# Check if tables exist, if not, create them
create_tables()

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
        youtube_url = request.form["youtube_url"]
        if youtube_url:
            comments, total_comments = get_video_comments(youtube_url)
            if comments:
                # Load spam detection model
                loaded_model, loaded_vect = load('best_model.pkl')
                spam_results = []
                for comment in comments:
                    # Transform comment and predict spam
                    new_comment = [comment]
                    new_comment_transformed = loaded_vect.transform(new_comment).toarray()
                    prediction = loaded_model.predict(new_comment_transformed)[0]
                    accuracy = loaded_model.predict_proba(new_comment_transformed)[0][1] * 100  # Convert accuracy to percentage
                    if prediction == 1:
                        spam_results.append(("Spam", accuracy, comment))  # Reordered the tuple
                    else:
                        spam_results.append(("Not Spam", accuracy, comment))  # Reordered the tuple
                
                # Process comments for spam detection or any other task
                return render_template("final.html", comments=spam_results, total_comments=total_comments)
            else:
                return render_template("final.html", result="No comments available on the YouTube video")
        else:
            return render_template("final.html", result="Please provide a valid YouTube URL")
    
    return render_template("final.html")

@app.route("/admin", methods=["GET","POST"])
def admin():
    if request.method == "POST":
        admin_username = "admin"
        admin_password = "admin"
        user = request.form["name"]
        password = request.form["pass"]
        if user == admin_username and password == admin_password:
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
