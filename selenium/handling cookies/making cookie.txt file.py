#helps to make cookie.txt file
from selenium import webdriver
import time
import json

driver=webdriver.Chrome("../chromedriver.exe")

try:
    driver.get("https://www.facebook.com")
    input("Done?")
    driver.find_element_by_xpath('//*[@id="u_0_b"]').click()
    time.sleep(5)
    json.dump(driver.get_cookies(),open("cookies.txt","w"))
    #print(driver.getcookies())
    
finally:
    driver.quit()
