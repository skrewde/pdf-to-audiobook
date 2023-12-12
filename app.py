"""
this python module defines the logic and routes for pdf-to-audiobook
"""
import os
import tempfile
from flask import (Flask, render_template, send_file)
import pyttsx3
from cs50 import SQL

# configure app
app = Flask(__name__)

# configure database using cs50 library
# db = SQL()

# instantiate pyttsx3 object
engine = pyttsx3.init()

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

@app.route("/tts")
def tts():
    text = "Fine weather we've got here, no?"

    # Use a temporary file to store the TTS audio
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_audio:
        temp_filename = temp_audio.name
        engine.save_to_file(text, temp_filename)
        engine.runAndWait()

    # Set the appropriate headers for the response
    response_headers = {
        'Content-Type': 'audio/mpeg',
        'Content-Disposition': f'attachment; filename={temp_filename}'
    }

    # Send the file as a response
    return send_file(temp_filename, as_attachment=True, download_name="test.mp3")


if __name__ ==  "__main__":
    app.run(debug=True)
