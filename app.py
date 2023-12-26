"""logic and routes for pdf-to-audiobook"""
import os
import secrets
import time

from flask import Flask, redirect, request, render_template, url_for
import flask_uploads as fu

import fitz
import pyttsx3
import pdfminer.high_level as pm

app = Flask(__name__)

app.config["UPLOADED_PDFS_DEST"] = "uploads/" # configure file path
app.config["MAX_CONTENT_LENGTH"] = 3 * 1024 * 1024 # set max upload size to 3 megabytes
app.config["SECRET_KEY"] = str(secrets.SystemRandom().getrandbits(128))

pdfs = fu.UploadSet("pdfs", extensions="pdf") # uploadset config
fu.configure_uploads(app, pdfs) # store pdf uploadset config in app instance

engine = pyttsx3.init() # instantiate pyttsx3 object


# define file processing functions for readability
def extract_text_from_pdf(pdf_path):
    """ extract text using pdfminer.six """
    return pm.extract_text(pdf_path)

def extract_text_from_pdf_pymupdf(pdf_path):
    """ extract text using pymupdf """
    all_text = ""
    i = 0

    doc = fitz.open(pdf_path) # open pdf

    for page in doc: # iterate the document pages
        print(f"working on page{i}...")
        text = page.get_text() # get plain text (is in UTF-8)

        i = i+1
        all_text += text
        # convert_text_to_audio(text, "uploads/test.mp3")

    return all_text


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
    """ create "audiobook" using pyttsx3 """
    engine.save_to_file(text, filename=audio_path)
    engine.runAndWait()

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
            # later: check if file is present
            # if not request.form.get("pdf"):
            #     print("Also true")
            #     return redirect(url_for("root", error="no_file"))

            # save pdf in "uploads", store name (minus extension) in filename
            pdf = pdfs.save(request.files["pdf"])
            filename = pdf.split(".")[0]
            print(f"{filename}.pdf was saved!")

            pdf_path = "uploads/" + pdf

            print("Extracting text...")
            text = extract_text_from_pdf_pymupdf(pdf_path)
            print("Finished extracting text!")

            # text_path = "uploads/pdf.txt"
            # save_string_to_text_file(text, text_path)
            # text_file_checker(text, text_path)
            audio_path = f"uploads/{filename}.mp3"

            print("Converting to audio...")
            audio_start_time = time.time()
            convert_text_to_audio(text, audio_path)
            audio_end_time = time.time()
            audio_run_time = audio_end_time - audio_start_time
            print(f"Audio took {audio_run_time} seconds to complete")
            print("Finished converting to audio!")

            return "Success! Check your uploads folder for the mp3 file"
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
