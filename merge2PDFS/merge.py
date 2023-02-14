from PyPDF2 import PdfMerger
merging = PdfMerger()
pdfs = [r"C:\Users\vijay\OneDrive\Desktop\short projects\audio recorder\0.pdf",r"C:\Users\vijay\OneDrive\Desktop\short projects\audio recorder\1.pdf"]
for pdf in pdfs:
  merging.append(pdf)
merging.write(r"C:\Users\vijay\OneDrive\Desktop\short projects\merge2PDFS\merged.pdf")
merging.close()
