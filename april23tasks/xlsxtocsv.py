import xlrd
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def csv_from_excel():
    wb = xlrd.open_workbook('icici_final.xlsx')
    sh = wb.sheet_by_name('Sheet1')
    icici_companies = open('icici_final.csv', 'w')
    wr = csv.writer(icici_companies, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

    icici_companies.close()

csv_from_excel()