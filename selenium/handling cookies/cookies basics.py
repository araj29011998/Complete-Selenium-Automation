
from selenium import webdriver
import time

driver=webdriver.Chrome()

try:
    print(driver.get_cookies())
    cookie={"name":"any_value","value":"any_value","myname":"Abhishek","domain":"www.google.com"}
    driver.get("https://www.google.com/")
    driver.add_cookie(cookie)
    print(driver.get_cookies())
    driver.delete_cookie("any_value") #take value of cookie's name key
    #driver.delete_all_cookies()
    time.sleep(2)

finally:
    driver.quit()