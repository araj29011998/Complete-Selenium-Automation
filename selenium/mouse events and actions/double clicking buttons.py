#action chains 
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
 

driver=webdriver.Chrome("../chromedriver.exe")

ac=ActionChains(driver)

driver.get("http://demo.guru99.com/test/simple_context_menu.html")
    
try:
    element=driver.find_element_by_xpath('//*[@id="authentication"]/button')
    #double click the element
    ac.click(element)
    ac.click(element)
    #or use this- ac.double_click(element)
    ac.perform()
    time.sleep(2)
    
    #switch to alert
    alert=driver.switch_to.alert
    alert.accept()
    time.sleep(3)

finally:
    driver.quit()