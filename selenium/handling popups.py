#handling popups from https://www.seleniumeasy.com/test/javascript-alert-box-demo.html
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()

driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")

driver.find_element_by_xpath("//*[@id='easycont']/div/div[2]/div[3]/div[2]/button").click()

#handling alert
alert=driver.switch_to_alert()
time.sleep(5)
#printing alert message
print(alert.text)
#to enter name
alert.send_keys("Abhishek")
time.sleep(5)
#to click on "OK"
alert.accept()
time.sleep(5)

#to click on "cancel"
#alert.dismiss()

driver.quit()

