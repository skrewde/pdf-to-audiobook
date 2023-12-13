"""
this python module defines the logic and routes for pdf-to-audiobook
"""

import os
import secrets

from flask import Flask, redirect, request, render_template, send_file, url_for
import flask_uploads as fu
from werkzeug.exceptions import RequestEntityTooLarge

import pyttsx3
from cs50 import SQL

app = Flask(__name__)

# uploadset config
pdfs = fu.UploadSet("pdfs", ["pdf"])

app.config["UPLOADED_PDFS_DEST"] = "uploads/"
app.config["MAX_CONTENT_LENGTH"] = 3 * 1024 * 1024 # set max upload size to 3 megabytes
app.config["SECRET_KEY"] = str(secrets.SystemRandom().getrandbits(128))

# store pdf uploadset config in app instance
fu.configure_uploads(app, pdfs)

# configure database using cs50 library
# db = SQL()

# instantiate pyttsx3 object
# engine = pyttsx3.init()

# logic for parsing pdf

# logic for converting, saving text to audio


# decorator for defining the root url
@app.route("/")
def root():
    """
    this function handles the route for the root url
    """
    return render_template("index.html")

# decorator for defining the convert url
@app.route("/", methods=["GET", "POST"])
def upload():
    """
    this function handles pdf uploads after page load
    """
    # uploaded_file = pdfs.save(request.files["pdf"])
    try:
        print('sup')
        # logic logic later
    except RequestEntityTooLarge:
        return redirect(url_for('root', error='file_size_limit_exceeded'))

# @app.route("/tts")
# def tts():
#     text = "Fine weather we've got here, no?"

#     # Use a temporary file to store the TTS audio
#     with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio:
#         temp_filename = temp_audio.name
#         engine.save_to_file(text, temp_filename)
#         engine.runAndWait()

#     # Set the appropriate headers for the response
#     response_headers = {
#         'Content-Type': 'audio/mpeg',
#         'Content-Disposition': f'attachment; filename={temp_filename}'
#     }

#     # Send the file as a response
#     return send_file(temp_filename, as_attachment=True, download_name="test.mp3")


if __name__ == "__main__":
    app.run(debug=True)
