import time
from selenium import webdriver

driver=webdriver.Chrome()

try:
    driver.get("http://demo.automationtesting.in/Frames.html")
    
    #switching to frame
    frame_element=driver.find_element_by_xpath("//*[@id='singleframe']")
    driver.switch_to.frame(frame_element)
    
    driver.find_element_by_xpath("/html/body/section/div/div/div/input").send_keys("hi there")
    time.sleep(5)
    
    #now switch back to parent/default frame
    driver.switch_to.default_content()
    #or use this - driver.switch_to.parent_frame()
    driver.find_element_by_xpath("//*[@id='header']/nav/div/div[2]/ul/li[1]/a").click()
    time.sleep(3)
    
finally:
    driver.quit()
    
