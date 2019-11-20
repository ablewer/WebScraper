import openpyxl
from openpyxl.utils import get_column_letter

excel_file = openpyxl.Workbook()

print(excel_file)

sheet = excel_file.active

print(sheet)

print(excel_file.sheetnames)

for i in range(1, 5):
    cell = str(get_column_letter(i) + '1')

    print(cell)

    sheet[cell] = 5

excel_file.save('ShawnTestData.xlsx')

excel_file.close()
