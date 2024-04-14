from flask import Flask, render_template,request, jsonify, session, flash, redirect, url_for
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import sqlite3
from joblib import dump, load
from sklearn.ensemble import ExtraTreesClassifier
app = Flask(__name__)
app.secret_key="ygfdffsfi99"
database="data1.db"
con=sqlite3.connect(database)
cur=con.cursor()
cur.execute("create table if not exists user(pid integer primary key,user_name text,number integer,mail text,password text)")
cur.execute("create table if not exists result(pid integer primary key,user_name text,comment text,result text)")
con.commit()
@app.route("/")
@app.route("/index1")
def index1():
    con=sqlite3.connect(database)
    cur=con.cursor()
    cur.execute("select * from result")
    data=cur.fetchall()
    data1=len(data)
    return render_template("index1.html",data=data1)

    
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
        return render_template("final.html" ,result="**successfully your profile registered**")
    return render_template("index1.html")

name1=[]
@app.route("/login", methods=["GET","POST"])
def login():
    if request.method=="POST":
        name=request.form["name"]
        name1.append(name)
        password=request.form["pass"]
        conn=sqlite3.connect(database)
        cur=conn.cursor()
        cur.execute("select * from user where user_name=? and password=?",(name,password,))
        data=cur.fetchone()
        if data:
            return render_template("spam.html")
        else:
            return "password mismatch"
    return render_template("index1.html")

@app.route("/spam", methods=["GET","POST"])
def spam():
    if request.method=="POST":
        comment=request.form["comment"]
        loaded_model, loaded_vect = load('ExtraTreesClassifier.pkl')
        new_comment = [comment]
        new_comment_transformed = loaded_vect.transform(new_comment).toarray()
        prediction = loaded_model.predict(new_comment_transformed)[0]
        if prediction == 1:
            prediction="spam"
            conn=sqlite3.connect(database)
            cur=conn.cursor()
            #print(name1[-1])
            cur.execute("insert into result (user_name,comment,result)values(?,?,?)",(name1[-1],comment,prediction))
            conn.commit()
            return render_template("final.html" ,result="The comment is spam")
        else:
            return render_template("final.html" ,result="The comment is not spam")
    return render_template("spam.html")
        

@app.route("/admin", methods=["GET","POST"])
def admin():
        a="admin"
        b="admin"
        user=request.form["name"]
        password=request.form["pass"]
        if user==a and password==b:
            conn=sqlite3.connect(database)
            cur=conn.cursor()
            cur.execute("select * from result")
            result=cur.fetchall()
            #print(result)
            return render_template("result.html",result=result)
        else:
            return"password mismatch"
    
        
            

if __name__=="__main__":
    app.run(debug=False,port=300)
    

