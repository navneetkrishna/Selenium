from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('http://localhost/coolsite')

print(driver.title)
print(driver.current_url)
print(driver.page_source)

time.sleep(2)
driver.quit()
