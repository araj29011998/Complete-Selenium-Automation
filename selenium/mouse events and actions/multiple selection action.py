import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("../chromedriver.exe")

ac=ActionChains(driver)

driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
driver.maximize_window()
dropdown_element=driver.find_element_by_id("multi-select")

select_tag=Select(dropdown_element)
options=select_tag.options
#press ctrl
ac.key_down(Keys.CONTROL)
#select all 
for option_element in options:
    ac.click(option_element)
#release ctrl
ac.key_up(Keys.CONTROL)
ac.perform()
time.sleep(5)

driver.find_element_by_id("printAll").click()

time.sleep(5)

driver.quit()
