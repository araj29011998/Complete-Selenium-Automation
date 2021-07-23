#waits in slenium
from selenium import webdriver
import time

driver=webdriver.Chrome()

#implicite wait- check again and again after 5 sec
driver.implicitly_wait(5)
driver.get("http://www.seleniumframework.com/practiceform/")
element=driver.find_element_by_id("periodicElement")

print(element.text)

driver.quit()