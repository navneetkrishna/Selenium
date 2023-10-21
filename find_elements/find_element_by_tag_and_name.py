from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('http://localhost/coolsite/')

paged = driver.find_element(By.NAME, 'paged')
print(paged)

links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links))
driver.quit()
