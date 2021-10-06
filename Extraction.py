import PyPDF2
from PyPDF2 import PdfFileWriter, PdfFileReader
import glob
import os
from getAllFiles import list_of_files
from pattern import find_pattern

def move_files(src, dst):
    '''
    src = path to file (.pdf)
    dst = new path to file (.pdf)
    '''
    try:
        os.replace(src, dst)
    except:
        os.rename(src, dst)

def extractFromInvoiceReport(path):
    #path = rf"C:\Users\4501531\OneDrive - Signode Industrial Group\Desktop\Sid's Work\Test Python\Invoice edits"
    move_to = rf"C:\pickticket_test\OneDrive - Signode Industrial Group\Invoice Report Validation (Darlene Only)\Invoice Report Validation files\Invoice Report from SX\Invoice Report Archive"
    order_no = []
    files = list_of_files(path)
    for pdf in files:

        # fileobj = open(pdf, 'rb')
        with open(pdf, 'rb') as fileobj:
            input_file = PdfFileReader(fileobj, strict='False')
            pages = input_file.numPages

                
            for page in range(pages):
                file_writer = PyPDF2.PdfFileWriter()
                get_page = input_file.getPage(page)
                #print(get_page)    
                master_text = get_page.extractText()
                #print(master_text)
                    
                temp = find_pattern(r'(\d{7})[-](\d{2})', master_text)
                for order in temp:
                    order_no.append(order.group(0))

        move_to = move_to + rf"\{os.path.basename(pdf)}"
        move_files(pdf, move_to)
    return order_no        
       
    #InvoicePdf = open(pdf, 'r')
    #InvoicePdfreader = PyPDF2.InvoicePdfreader(InvoicePdf)
    #pages = InvoicePdfreader.numPages

#print(extractFromInvoiceReport(rf"C:\Users\4501531\OneDrive - Signode Industrial Group\Desktop\Sid's Work\Test Python\Invoice edits"))

