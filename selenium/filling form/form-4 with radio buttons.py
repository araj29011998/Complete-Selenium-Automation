#working radio buttons
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("../chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")

radio_buttons=driver.find_elements(By.NAME,"optradio")

time.sleep(1)
radio_buttons[0].click()
time.sleep(2)
radio_buttons[1].click()
time.sleep(4)


#group radio buttons demo
radio_buttons=driver.find_elements(By.NAME,"ageGroup")

time.sleep(1)
radio_buttons[0].click()
time.sleep(2)
radio_buttons[1].click()
time.sleep(4)
radio_buttons[2].click()
time.sleep(2)

driver.quit()