import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("../chromedriver.exe")

ac=ActionChains(driver)

driver.get("https://www.w3schools.com/howto/howto_html_file_upload_button.asp")

try:
    element=driver.find_element_by_id("myFile")
    element.send_keys("C:\\Users\\Hp\\Pictures\\2.png")
    time.sleep(3)
    
finally:
    driver.quit()