from flask import render_template, request, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import FileField
import os
import pyttsx3
from PyPDF2 import PdfReader

from app import app

class UploadForm(FlaskForm):
    pdf_file = FileField('PDF File')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()

    if form.validate_on_submit():
        pdf_file = form.pdf_file.data
        audiobook_path = convert_pdf_to_audio(pdf_file)
        flash('Audiobook generated successfully!', 'success')
        return redirect(url_for('index'))

    return render_template('index.html', form=form)

def convert_pdf_to_audio(pdf_file):
    output_path = 'output.mp3'
    text = extract_text_from_pdf(pdf_file)
    generate_audio_from_text(text, output_path)
    return output_path

def extract_text_from_pdf(pdf_file):
    with open(pdf_file, 'rb') as file:
        reader = PdfReader(file)
        text = ''
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
        return text

def generate_audio_from_text(text, output_path):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_path)
    engine.runAndWait()
