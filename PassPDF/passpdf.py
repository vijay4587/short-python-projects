from PyPDF2 import PdfWriter, PdfReader
output,pdffile = PdfWriter(),PdfReader(r"C:\Users\vijay\OneDrive\Desktop\short projects\PassPDF\iesc112.pdf")
n = len(pdffile.pages)
for index in range(n):
  pages = pdffile.pages[index]
  output.add_page(pages)

passW = input("Enter password: ")
output.encrypt(passW)
with open(r"C:\Users\vijay\OneDrive\Desktop\short projects\PassPDF\encrypted.pdf","wb") as f:
  output.write(f)