from pypdf2 import PdfFileWriter , PdfFileReader

ouput_result_pdf = PdfFileWriter() 

file_pdf = open("test.pdf", "rb")
file_pdf2 = open("test1.pdf", "rb")
reader_presentation = PdfFileReader(file_pdf)
reader_rep = PdfFileReader(file_pdf2)
print("Number of pages:" + str(reader_rep.getNumPages()))


ouput_result_pdf.addPage(reader_presentation.getPage(0).rotateClockwise())
for i in range(reader_rep.getNumPage()):
    ouput_result_pdf.addPage(reader_presentation.getPage(0))
    ouput_result_pdf.addPage(reader_presentation.getPage(1))


file_pdf = open("test.pdf", "wb")

ouput_result_pdf.write(file_pdf)
file_pdf.close()
file_pdf2.close()


