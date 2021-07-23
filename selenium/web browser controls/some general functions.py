import time
from selenium import webdriver

driver=webdriver.Chrome("../chromedriver.exe")

try:
    driver.get("https://www.youtube.com/")
    #take screenshot and save in current directory as youtube.png
    #driver.save_screenshot("./youtube.png")
    
    #maximizing the window
    #driver.maximize_window()
    
    #toggle fullscreen
    #driver.fullscreen_window()
    
    #position of window
    print(driver.get_window_position())
    
    #change window postion by +500 to x
    window_position=driver.get_window_position()
    window_position["x"]+=500
    driver.set_window_position(x=window_position["x"],y=window_position["y"])
    #or use this
    #driver.set_window_position(**window_position)
    
    #window size
    window_size=driver.get_window_size()
    #half the window size
    window_size["width"]//=2
    driver.set_window_size(**window_size)
    print(window_size)
    
    #get the page source
    open("source.html","w",encoding="utf-8").write(driver.page_source)
    time.sleep(3)  

except:
    driver.quit()
