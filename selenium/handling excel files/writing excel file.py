import xlwt

workbook=xlwt.Workbook()

worksheet=workbook.add_sheet("sample-data")

#worksheet.write(0,0,"abhi")
#worksheet.write(0,1,1998)

#workbook.save("./my-data.xls")

#add table of 9
number=9
table=[]

for i in range(1,11):
    table.append(["%d X %d"%(number,i),number*i])
    
for i in range(10):
    for j in range(2):
        worksheet.write(i,j,table[i][j])
    
workbook.save("./multiplcation_table.xls")