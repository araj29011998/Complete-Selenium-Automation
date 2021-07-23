#usage of all find_element_by methods
from selenium import webdriver

import time

from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()

driver.get("https://www.google.com")

time.sleep(1)
testfield=driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
#testfield=driver.find_element_by_name('q')

testfield.send_keys("Hello world"+Keys.RETURN)

time.sleep(2)

home_button=driver.find_element_by_id("logo")
home_button.click()
time.sleep(2)

driver.quit()