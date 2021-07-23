
from selenium import webdriver
import time 
import json 

cookies=json.load(open("cookie.txt","r"))

driver=webdriver.Chrome("../chromedriver.exe")

driver.get("https://www.facebook.com")

try:
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    time.sleep(5)

finally:
    driver.quit()