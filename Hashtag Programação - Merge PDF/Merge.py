import PyPDF2
import os

merger = PyPDF2.PdfMerger()

lista = os.listdir('pdfs')

for pdf in lista:
    if '.pdf' in pdf:
        merger.append(f'pdfs/{pdf}')

merger.write('PDF.pdf')
