"""
module to test page count function?
"""
import fitz

doc = fitz.open("uploads/test.pdf") # open a document

out = open("test.txt", "wb") # create a text output

for page in doc: # iterate the document pages
    text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
    out.write(text) # write text of page
    out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
    
out.close()




# from pdfminer.pdfdocument import PDFDocument
# from pdfminer.pdfparser import PDFParser
# from pdfminer.pdftypes import resolve1

# with open('/uploads/test.pdf', 'rb') as f:
#     parser = PDFParser(f)
#     doc = PDFDocument(parser)

#     parser.set_document(doc)
#     pages = resolve1(doc.catalog['Pages'])
#     pages_count = pages.get('Count', 0)
