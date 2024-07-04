import os
import sys
from PyPDF2 import PdfReader, PdfWriter
import yaml

INPUT_PDF = ""
OUTPUT_NAME = ""
OUTDIR = ""

def split(path, name_of_split, numlow, numhigh):
    pdf = PdfReader(path)
    pdf_writer = PdfWriter()
    for page in range(numlow, numhigh+1):
        pdf_writer.add_page(pdf.pages[page])
    output = f'{name_of_split}{numlow}_{numhigh}.pdf'
    with open(output, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)



try:
    with open('config.yml', 'r') as file:
         config = yaml.safe_load(file)

    INPUT_PDF = config['paths']['inputfile']
    OUTPUT_NAME = config['paths']['outputname']
    OUTDIR = config['paths']['outputdir']
except OSError:
    print(f'File config.yml not found. Needs to be in same directory as extractpdf')


try:
    # Command line mode
    if sys.argv[1] == "-p":
        page = sys.argv[2]
        if "-" in page:
            numlist = str.split(page, '-')
            numlow = int(numlist[0])
            numhigh = int(numlist[1])
            split(INPUT_PDF, f'{OUTDIR}{OUTPUT_NAME}', numlow, numhigh)
            #os.system(f"qpdf {INPUT_PDF} --pages . {numlow}-{numhigh} -- {OUTDIR}{OUTPUT_NAME}{numlow}_{numhigh}.pdf")
        else:
            numlow = int(int(page))
            numhigh = int(int(page))
            split(INPUT_PDF, f'{OUTDIR}{OUTPUT_NAME}', numlow, numhigh)
            #os.system(f"qpdf {INPUT_PDF} --pages . {numlow}-{numhigh} -- {OUTDIR}{OUTPUT_NAME}{numlow}_{numhigh}.pdf")
        exit()
except IndexError:
    # Interactice mode
    prange = input("Enter page range (pagenum-pagenum):")
    if ("-" in prange):
        numlist = str.split(prange, '-')
        numlow = int(numlist[0])
        numhigh = int(numlist[1])
        split(INPUT_PDF, f'{OUTDIR}{OUTPUT_NAME}', numlow, numhigh)
        #os.system(f"qpdf {INPUT_PDF} --pages . {numlow}-{numhigh} -- {OUTDIR}{OUTPUT_NAME}{numlow}_{numhigh}.pdf")
    else:
        numlow = int(int(prange))
        numhigh = int(int(prange))
        split(INPUT_PDF, f'{OUTDIR}{OUTPUT_NAME}', numlow, numhigh)
        #os.system(f"qpdf {INPUT_PDF} --pages . {numlow}-{numhigh} -- {OUTDIR}{OUTPUT_NAME}{numlow}_{numhigh}.pdf")
