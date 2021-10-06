import os
import glob
from pattern import find_pattern
def list_of_pdf(path):
    #path = rf"C:\Users\4501531\OneDrive - Signode Industrial Group\Desktop\Sid's Work\Test Python\Invoice edits\Invoiced pick tickets"
    pdf_order_list = []
    file_list = os.listdir(path)
    for pdf in file_list:
        temp1 = find_pattern(r'(\d{7})[-](\d{2})', pdf)
        for temp in temp1:
            pdf_order_list.append(temp.group(0))
    return pdf_order_list   

#print(list_of_pdf(rf"C:\Users\4501531\OneDrive - Signode Industrial Group\Desktop\Sid's Work\Test Python\Invoice edits\Invoiced pick tickets"))