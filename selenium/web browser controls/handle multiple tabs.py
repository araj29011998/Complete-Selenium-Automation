import time
from selenium import webdriver

driver=webdriver.Chrome("../chromedriver.exe")

try:
    driver.get("http://book.theautomatedtester.co.uk/chapter1")
    print(driver.window_handles)
    driver.find_element_by_class_name("multiplewindow").click()
    print(driver.window_handles) #return a list of all open window_handles
    
    #finding current window handle
    print(driver.current_window_handle)
    #switch to a particular window
    #driver.switch_to.window(window_handle)
    
    #switch to last opened window
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(3)
    #close that window only
    driver.close() #close the current window_handle
    time.sleep(3)
finally:
    driver.quit()  #close all the window handles