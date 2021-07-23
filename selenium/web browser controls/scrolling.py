import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("../chromedriver.exe")


driver.get("https://ui.vision/rpa/docs/selenium-ide/executescript")


#scrolling ways
#1st way- to get at 1000 point
#driver.execute_script("window.scrollBy(0,1000);")

#2nd way- to scroll at the end of webpage
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")

#3rd way- to scroll till a particular element
driver.execute_script("var ele=document.getElementById('getdate'); ele.scrollIntoView();")

#different method of writing above
#ele=driver.find_element_by_id("getdate")
#driver.execute_script('argument[0].scrollIntoView()',ele)

time.sleep(3)

driver.quit()