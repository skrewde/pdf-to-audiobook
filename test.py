"""
module to test page count function?
"""
import time

import fitz
import pyttsx3
import pdfminer.high_level as pm

start_time = time.time()

engine = pyttsx3.init() # instantiate pyttsx3 object

doc = fitz.open("uploads/test.pdf") # open a document

all_text = ""

def convert_text_to_audio(txt_path, audio_path):
    """ create "audiobook" using pyttsx3 """
    engine.save_to_file(txt_path, filename=audio_path)
    engine.runAndWait()

# test for pymupdf
start = time.time()
with open("uploads/test.txt", "w", encoding="utf-8") as out: # create a text output
    i = 0

    for page in doc: # iterate the document pages
        print(f"working on page{i}...")
        text = page.get_text() # get plain text (is in UTF-8)
        out.write(text) # write text of page
        out.write("\f") # write page delimiter (form feed 0x0C)
        i = i+1
        all_text += text
        # convert_text_to_audio(text, "uploads/test.mp3")
    out.close()
end = time.time()

elapsed_time = end - start

print(f"PyMuPDF's time for processing is {elapsed_time}")

doc.close() # close doc object

# test for pdfminer
start = time.time()
with open("uploads/test.pdf", "rb") as file:
    text = pm.extract_text(file)

    with open("uploads/test1.txt", "w", encoding="utf-8") as text_file:
        text_file.write(text)
end = time.time()

elapsed_time = end - start

print(f"PdfMiner.Six's time for processing is {elapsed_time}")

end_time = time.time()

print(f"the total running time is {end_time - start_time}")
