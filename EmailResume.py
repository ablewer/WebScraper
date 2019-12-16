import smtplib, openpyxl

emailDict = {}  # does what it says haha - email dictionary

def emailResume(dict):
    wb = openpyxl.load_workbook('Excel_Data.xlsx')  # load the excel file
    sheets = wb.sheetnames  # load the names of all the sheets
    iterator = 0
    for sheet in sheets:
        emailCell = sheet.cell(row=1, column=6)
        if emailCell.value == 'Email':
            for row in range(2, sheet.max_row):
                dict[sheet] = sheet['F' + str(row)]

