from flask import Flask, request,render_template, redirect
import os
import sqlite3

# to set path  and location of file
currentlocation = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__=="__main__":
  app.run(debug=True)

   