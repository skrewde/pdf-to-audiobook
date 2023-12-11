"""
this python module defines the logic and routes for pdf-to-audiobook
"""
from flask import Flask, render_template
# from cs50 import SQL

# configure app
app = Flask(__name__)

# configure database using cs50 library
# db = SQL()

# decorator for defining the root url
@app.route("/")
def root():
    """
    this function handles the route for the root url
    """
    return "Yo, this is the app"

# decorator for defining the convert url
@app.route("/convert")
def convert():
    """
    this function handles the route for the convert url
    """
    return "Yo, this is for conversion"

if __name__ ==  "__main__":
    app.run(debug=True)
