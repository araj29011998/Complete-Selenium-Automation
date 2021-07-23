import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome("../chromedriver.exe")

ac=ActionChains(driver)

driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")

try:
     driver.find_element_by_xpath('//*[@id="table-files"]/tbody/tr[1]/td[5]/a[1]').click()
     time.sleep(5)
finally:
    driver.quit()