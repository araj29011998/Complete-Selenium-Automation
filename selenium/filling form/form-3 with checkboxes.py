import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome("../chromedriver.exe")

driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")

tick=driver.find_element(By.ID,"isAgeSelected")
#conditional commands: is_selected()
print("Before clicking:",tick.is_selected())

tick.click()

print("After clicking:",tick.is_selected())

time.sleep(5)
tick1=driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[2]/div[1]/label/input")
tick2=driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[2]/div[2]/label/input")
tick3=driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[2]/div[3]/label/input")
tick4=driver.find_element(By.XPATH,"/html/body/div[2]/div/div[2]/div[2]/div[2]/div[4]/label/input")

time.sleep(10)

uncheck=driver.find_element(By.ID,"check1").click()

time.sleep(5)
driver.quit()

