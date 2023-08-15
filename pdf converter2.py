from pypdf2 import PdfFileWriter , PdfFileReader

f= open("recap.pdf", "rb")
reader = PdfFileReader()
page0.getPage(0)
text = page0.extractText()
text = text.replace("Ò", '"').replace("‘", "è").replace("‹", "à").replace("”", "é").replace("Õ", "'").replace("’", "ê")
f.close()
print(text)
