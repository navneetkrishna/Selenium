from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('http://localhost/coolsite/shop')
driver.maximize_window()

time.sleep(2)

# text() function to click on Sample Page
driver.find_element(By.XPATH, '//*[text()="Sample Page"]').click()

# chained XPath function to click on Sample Page
driver.find_element(By.XPATH, '//*[text()="Sample Page"]').click()


time.sleep(2)
driver.quit()