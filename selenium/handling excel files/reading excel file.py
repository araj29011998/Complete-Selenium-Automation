
import xlrd

workbook=xlrd.open_workbook("data.xlsx")

#selecting a particular sheet
worksheet=workbook.sheet_by_index(0)

print(worksheet.cell_value(1,1))

print("rows:",worksheet.nrows,"cols:",worksheet.ncols)

data=[]

for row_no in range(worksheet.nrows):
    row_data=[]
    for col_no in range(worksheet.ncols):
        row_data.append(worksheet.cell_value(row_no,col_no))
    data.append(row_data)

print(data)
print(len(data))

for row_no in range(len(data)):
    for col_no in range(len(data[row_no])):
        print(data[row_no][col_no],end="\t")
    print()