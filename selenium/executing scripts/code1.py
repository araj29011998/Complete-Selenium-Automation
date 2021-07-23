
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("../chromedriver.exe")


driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

message="hello world"
#filling value using webelement interface
#driver.find_element(By.ID,"user-message").send_keys(message)

script='document.getElementById("user-message").value="Hello World";'
#using execute script function
driver.execute_script(script)

driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button").click()

