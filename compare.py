import os
from list_pdf import list_of_pdf
from Extraction import extractFromInvoiceReport

#create an email object
import win32com.client

def run_compare():
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = 'dmcmartin@signode.com'
    mail.Subject = 'Invoice register report - Discrepencies'
    #mail.HTMLBody = '<h3>This is HTML Body</h3>'
    mail.Body = "Please find the list of order no.s from Invoice register report that were not found in picktickets list - \n *** \n \n"
    #mail.Attachments.Add('c:\\sample.xlsx')
    #mail.Attachments.Add('c:\\sample2.xlsx')

    mail.CC = 's.patel@signode.com'

    not_in_invoice_report = []
    path_invoice_report = rf"C:\pickticket_test\OneDrive - Signode Industrial Group\Invoice Report Validation (Darlene Only)\Invoice Report Validation files\Invoice Report from SX"
    path_picktickets = rf"C:\pickticket_test\OneDrive - Signode Industrial Group\Invoice Report Validation (Darlene Only)\Invoice Report Validation files\Invoiced pick tickets"
    orderList_invoice_report = extractFromInvoiceReport(path_invoice_report)
    orderList_picktickets = list_of_pdf(path_picktickets)

    for i in orderList_invoice_report:
        if i not in orderList_picktickets:
            not_in_invoice_report.append(i)

    nice_table =""
    for i in range(len(not_in_invoice_report)):
        nice_table += not_in_invoice_report[i] + " \n"

    nice_table += "\n ***"
    mail.Body += nice_table

    if orderList_picktickets and orderList_invoice_report:
        mail.Send()
        print(not_in_invoice_report)
    else:
        print("---------------------------------------")
        print("---------------------------------------")
        print("Skipped run")
        print("---------------------------------------")
        print("---------------------------------------")


# print(orderList_invoice_report)
# print(orderList_picktickets)
