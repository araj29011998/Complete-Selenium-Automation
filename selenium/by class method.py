#usage of by class method 
from selenium import webdriver

import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.google.com")

time.sleep(1)
#textfield=driver.find_element_by_name('q')
textfield=driver.find_element(By.NAME,"q")
textfield.send_keys("hi there"+Keys.RETURN)

driver.quit()