import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("../chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")

dropdown_element=driver.find_element_by_id("select-demo")

select_tag=Select(dropdown_element)
options=select_tag.options

for option in options:
    print(option.text)

for option in options:
    select_tag.select_by_value(option.get_attribute("value"))
    time.sleep(1)
