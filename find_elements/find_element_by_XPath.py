from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('http://localhost/coolsite/shop')
driver.maximize_window()

time.sleep(2)

# relative XPath to add album to cart
driver.find_element(By.XPATH, '''//a[@aria-label='Add “Album” to your cart']''').click()

# # absolute XPath to add album to cart
# driver.find_element(By.XPATH, '/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/ul[1]/li[1]/a[2]').click()


time.sleep(3)

driver.quit()
