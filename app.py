"""
this python module defines the logic and routes for pdf-to-audiobook
"""
import os
import sys
import secrets

# import werkzeug
from flask import Flask, redirect, request, render_template, url_for
import flask_uploads as fu

# import pyttsx3
import pdfminer.high_level as pm
# from cs50 import SQL

# import utils

app = Flask(__name__)

# uploadset config
pdfs = fu.UploadSet("pdfs", extensions="pdf")

# app.config["UPLOADED_PDFS_DEST"] = utils.set_destination(app, path="uploads/")
app.config["UPLOADED_PDFS_DEST"] = "uploads/"
app.config["MAX_CONTENT_LENGTH"] = 3 * 1024 * 1024 # set max upload size to 3 megabytes
app.config["SECRET_KEY"] = str(secrets.SystemRandom().getrandbits(128))

def 

# store pdf uploadset config in app instance
fu.configure_uploads(app, pdfs)

# configure database using cs50 library
# db = SQL()

# instantiate pyttsx3 object
# engine = pyttsx3.init()

# add logic for parsing pdf

# add logic for converting, saving text to audio

# decorator for defining the root url
@app.route("/")
def root():
    """
    this function handles the route for the root url
    """

    test2 = __name__ == "__main__"
    print(test2)
    return render_template("index.html")

@app.route("/", methods=["GET", "POST"])
def upload():
    """
    this function handles pdf uploads
    """

    if request.method == "POST" and "pdf" in request.files:
        try:
            # check if a file exists
            if not request.files["pdf"]:
                redirect(url_for("root", error="no_file"))

            # save pdf upload to the "uploads" folder
            filename = pdfs.save(request.files["pdf"])

            file_path = "uploads/" + filename

            text = pm.extract_text(file_path)

            with open("uploads/pdf.txt", "w", encoding="utf-8") as text_file:
                # write FILE variable to a txt file
                text_file.write(text)

            # check if the file exists
            if os.path.exists(file_path):
                # read text file
                with open(file_path, "r", encoding="utf-8") as file:
                    file_content = file.read()

                # compare the stripped versions of both files
                if text.strip() == file_content.strip():
                    print(len(text.strip()))
                    print(len(file_content.strip()))
                    print("Success! The string written to text file.")
                else:
                    print(len(text.strip()))
                    print(len(file_content.strip()))
                    print("Warning! Text file content differs from the original string.")
            # catch-all exception
            else:
                print("Failure! File not created.")

            print(f'haha, {filename} saved!')

            return "Your file uploaded successfully (Not really)!"
        except fu.UploadNotAllowed:
            return redirect(url_for("root", error="upload_not_allowed"))
    return render_template("index.html")

@app.errorhandler(413)
def file_size_limit_exceeded(error):
    """
    test for 413 error handling
    """
    return redirect(url_for("root", error="file_size_limit_exceeded"))

@app.errorhandler(404)
def not_found(error):
    """
    test for 404 error handling
    """
    return redirect(url_for("root", error="not_found"))

if __name__ == "__main__":
    app.run(debug=True)
