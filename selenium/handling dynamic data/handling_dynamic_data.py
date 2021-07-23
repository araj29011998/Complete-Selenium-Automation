#Printing details of 3 person appearing on site-"https://www.seleniumeasy.com/test/dynamic-data-loading-demo.html"
import time
from selenium import webdriver
driver=webdriver.Chrome("../chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/dynamic-data-loading-demo.html")

button=driver.find_element_by_id("save")

for i in range(3):
    button.click()
    time.sleep(5)
    details=driver.find_element_by_id("loading")
    print(details.text)

driver.quit()