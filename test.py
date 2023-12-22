"""
module to test page count function?
"""
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdftypes import resolve1

with open('/uploads/test.pdf', 'rb') as f:
    parser = PDFParser(f)
    doc = PDFDocument(parser)

    parser.set_document(doc)
    pages = resolve1(doc.catalog['Pages'])
    pages_count = pages.get('Count', 0)
