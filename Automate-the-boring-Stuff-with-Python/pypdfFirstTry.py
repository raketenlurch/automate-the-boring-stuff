import PyPDF2

pdfFileObj = open('facing-finance.pdf', 'rb')
pdfReader  = PyPDF2.PdfFileReader(pdfFileObj)
pdfReader.numPages
pageObj = pdfReader.getPage(0)
pageObj.extractText()