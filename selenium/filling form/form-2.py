#filling 2nd form and validating ans
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("../chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

num1=2
num2=3

element1=driver.find_element(By.ID,"sum1").send_keys(num1)
element2=driver.find_element(By.ID,"sum2").send_keys(num2)

button=driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button").click()

displayed_sum=driver.find_element(By.ID,"displayvalue").text

if (num1+num2) == int(displayed_sum):
    print("same")
else:
    print("different")

time.sleep(5)

driver.quit()
    

