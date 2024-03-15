import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfMerger()
    for pdf in pdf_list:
        print(f'Pdf processing Done... {pdf}')
        merger.append(pdf)
    merger.write('merge_file.pdf')
    merger.close()


pdf_combiner(inputs)
