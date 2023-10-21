from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb
import time

driver = webdriver.Firefox()
driver.get("http://localhost/coolsite/")

# adding item to cart using XPATH
add_item_to_cart = driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/main/ul/li[1]/a[2]')
add_item_to_cart.click()

time.sleep(2)

# visitMy account page using CSS selector
my_acc = driver.find_element(By.CSS_SELECTOR, '.nav-menu > li:nth-child(4) > a:nth-child(1)')
my_acc.click()

driver.quit()

