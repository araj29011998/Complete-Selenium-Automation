
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
 

driver=webdriver.Chrome("../chromedriver.exe")

ac=ActionChains(driver)

driver.get("https://artoftesting.com/mouse-hover-in-selenium-webdriver-java")
#since we can't scroll in drag and drop action, so lets maximize the window
driver.maximize_window()
try:
    element=driver.find_element_by_xpath('//*[@id="menu-item-97"]/a')
    element1=driver.find_element_by_xpath('//*[@id="menu-item-310"]/a')
    ac.move_to_element(element)
    ac.move_to_element(element1).click()
    ac.perform()
    time.sleep(5)
finally:
    driver.quit()