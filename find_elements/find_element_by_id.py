from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb
import time

driver = webdriver.Firefox()
driver.get("http://localhost/coolsite/")

cart = driver.find_element(By.ID, "site-header-cart")
cart.click()

time.sleep(3)

driver.quit()

 