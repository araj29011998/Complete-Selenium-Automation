from selenium import webdriver
import xlwt

driver=webdriver.Chrome("../chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/table-data-download-demo.html")

table=driver.find_element_by_tag_name("table")

#print(table)

#finding element inside table web element
head=table.find_element_by_tag_name("thead")
body=table.find_element_by_tag_name("tbody")

data=[]

for tr_tag in head.find_elements_by_tag_name("tr"):
    row_data=[]
    for th_tag in tr_tag.find_elements_by_tag_name("th"):
        row_data.append(th_tag.text)
    data.append(row_data)

for tr_tag in body.find_elements_by_tag_name("tr"):
    row_data=[]
    for th_tag in tr_tag.find_elements_by_tag_name("td"):
        row_data.append(th_tag.text)
    data.append(row_data)


workbook=xlwt.Workbook()
worksheet=workbook.add_sheet("employee_data")

for i in range(len(data)):
    for j in range(len(data[i])):
        worksheet.write(i,j,data[i][j])

workbook.save("./employee.xls")

driver.quit()