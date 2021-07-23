
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
 

driver=webdriver.Chrome("../chromedriver.exe")

ac=ActionChains(driver)

driver.get("http://demo.guru99.com/test/drag_drop.html")
#since we can't scroll in drag and drop action, so lets maximize the window
driver.maximize_window()
try:
    #ac.drag_and_drop(src_element,destination_element)
    src_element=driver.find_element_by_xpath('//*[@id="fourth"]/a')
    destination_element=driver.find_element_by_xpath('//*[@id="amt7"]/li')
    ac.drag_and_drop(src_element,destination_element)
    ac.perform()
    time.sleep(5)
finally:
    driver.quit()