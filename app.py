import pymongo
import os

from flask import Flask, render_template, redirect, request, url_for




#connect to database
app = Flask(__name__)





#home page


@app.route('/')
def home():
    return render_template("index.html")
    

    
if __name__ == '__main__':
    app.run(host=os.environ.get('0.0.0.0'),
            port=(os.environ.get('8000')),
            debug=True)
