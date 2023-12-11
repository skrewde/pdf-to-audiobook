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
