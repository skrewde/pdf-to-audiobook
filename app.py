"""logic and routes for pdf-to-audiobook"""
import os
import sys
import secrets

from flask import Flask, redirect, request, render_template, url_for
import flask_uploads as fu

import pyttsx3
import pdfminer.high_level as pm

app = Flask(__name__)

pdfs = fu.UploadSet("pdfs", extensions="pdf") # uploadset config

app.config["UPLOADED_PDFS_DEST"] = "uploads/"
app.config["MAX_CONTENT_LENGTH"] = 3 * 1024 * 1024 # set max upload size to 3 megabytes
app.config["SECRET_KEY"] = str(secrets.SystemRandom().getrandbits(128))

fu.configure_uploads(app, pdfs) # store pdf uploadset config in app instance

engine = pyttsx3.init() # instantiate pyttsx3 object

# define file processing functions for readability
def extract_text_from_pdf(pdf_path):
    """ extract text using pdfminer.six """
    return pm.extract_text(pdf_path)

def save_string_to_text_file(text, text_path):
    """ write a string variable (text) to a text file (@ text_path) """
    with open(text_path, "w", encoding="utf-8") as text_file:
        text_file.write(text)

def text_file_checker(text, text_path):
    """ compare string variable and text file """
    if os.path.exists(text_path):
        # read text file
        with open(text_path, "r", encoding="utf-8") as file:
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

def convert_text_to_audio(text, audio_path):
    """ function to create audiobook using pyttsx3 """
    engine.save_to_file(text, filename=audio_path)

# decorator for defining the root url
@app.route("/")
def root():
    """ function to handle the root url """
    return render_template("index.html")

@app.route("/", methods=["GET", "POST"])
def convert():
    """ function to handle pdf uploads """

    if request.method == "POST" and "pdf" in request.files:
        try:
            # check if file is present
            if not request.files["pdf"]:
                redirect(url_for("root", error="no_file"))

            # save pdf in "uploads", store name in filename
            filename = pdfs.save(request.files["pdf"])

            print(f"{filename} was saved!")

            pdf_path = "uploads/" + filename

            text = extract_text_from_pdf(pdf_path)

            # text_path = "uploads/pdf.txt"

            # audio_path = f"audio/{filename}.mp3"

            # save_string_to_text_file(text, text_path)

            # text_file_checker(text, text_path)

            convert_text_to_audio(text, audio_path)

            print(f"haha, {filename} saved!")
            return "Success! Check your folder for the mp3 file"
        except fu.UploadNotAllowed:
            return redirect(url_for("root", error="upload_not_allowed"))
    return render_template("index.html")

@app.errorhandler(413)
def file_size_limit_exceeded(error):
    """ error handling for 413 """
    return redirect(url_for("root", error="file_size_limit_exceeded"))

@app.errorhandler(404)
def not_found(error):
    """ error handling for 404 """
    return redirect(url_for("root", error="not_found"))

if __name__ == "__main__":
    app.run()
