# Manipulating pdfs using PyPDF2
import PyPDF2

pdfFileObj = open('Problem-Statement-1.pdf','rb')
# creating pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#printing no of pages
print(pdfReader.numPages)

#creating a page object
pageObj = pdfReader.getPage(0)

#extracting text from page
print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()
