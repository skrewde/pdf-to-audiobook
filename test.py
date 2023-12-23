"""
module to test page count function?
"""
import fitz
import pyttsx3

engine = pyttsx3.init() # instantiate pyttsx3 object

doc = fitz.open("uploads/test.pdf") # open a document

def convert_text_to_audio(text, audio_path):
    """ create "audiobook" using pyttsx3 """
    engine.save_to_file(text, filename=audio_path)
    engine.runAndWait()


out = open("test.txt", "wb") # create a text output

for page in doc: # iterate the document pages
    text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
    out.write(text) # write text of page
    out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
    convert_text_to_audio(text, "uploads/test.mp3")

# out.close()

# from pdfminer.pdfdocument import PDFDocument
# from pdfminer.pdfparser import PDFParser
# from pdfminer.pdftypes import resolve1

# with open('/uploads/test.pdf', 'rb') as f:
#     parser = PDFParser(f)
#     doc = PDFDocument(parser)

#     parser.set_document(doc)
#     pages = resolve1(doc.catalog['Pages'])
#     pages_count = pages.get('Count', 0)
