#testing back,forward,refresh method
import time
from selenium import webdriver
driver=webdriver.Chrome()

url="https://www.google.com"

driver.get(url)

time.sleep(2) 

driver.get("https://www.python.org")
time.sleep(2)

driver.refresh()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.close()