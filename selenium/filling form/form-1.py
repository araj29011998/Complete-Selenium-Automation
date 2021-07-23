#filling form and comparing displayed message, on this link- "https://www.seleniumeasy.com/test/basic-first-form-demo.html"
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("../chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

message="hello world"

driver.find_element(By.ID,"user-message").send_keys(message)

driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button").click()

#this will give error as we can't use find_element_by_class when class name has space in it
#driver.find_element(By.CLASS,"btn btn-default").click()

displayed_message= driver.find_element(By.ID,"display").text
time.sleep(5)
#compare entered message and displayed message
if message == displayed_message:
    print("same")
else:
    print("different")

driver.quit()