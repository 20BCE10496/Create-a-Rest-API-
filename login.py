from flask import Flask, request,render_template, redirect
import os
import sqlite3

# to set path  and location of file
currentlocation = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

@app.route('/login')
def homepage():
    return render_template("index.html")

@app.route('/login',methods=["POST"])
def checklogin():
    UN=request.form('Username')
    PW=request.form('Password')

    sqlconnection=sqlite3.Connection(currentlocation + "\Login.db")
    cursor=sqlconnection.cursor()


if __name__=="__main__":
  app.run(debug=True)

   