#context/right click

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
 

driver=webdriver.Chrome("../chromedriver.exe")

ac=ActionChains(driver)

driver.get("http://demo.guru99.com/test/simple_context_menu.html")
    
try:
    element=driver.find_element_by_xpath('//*[@id="authentication"]/span')
    element1=driver.find_element_by_xpath('//*[@id="authentication"]/ul/li[1]')
    ac.context_click(element)
    ac.click(element1)
    #Or use this - driver.find_element_by_xpath('//*[@id="authentication"]/ul/li[1]').click()
    ac.perform()
    time.sleep(3)
    #handling alert
    alert=driver.switch_to.alert
    print(alert.text)
    alert.accept()
    time.sleep(3)
    
finally:
    driver.quit()
