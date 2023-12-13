import os

def set_destination(app, path):
    return os.path.join(app.instance_path, path)

print(set_destination)


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