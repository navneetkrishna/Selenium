from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('http://localhost/coolsite/shop/my-account')
driver.maximize_window()

time.sleep(2)
# input to username
driver.find_element(By.CSS_SELECTOR, 'input[name=username]').send_keys('admin')

# input to password
driver.find_element(By.CSS_SELECTOR, 'input[name=password]').send_keys('admin')

# click on login button
driver.find_element(By.CSS_SELECTOR, 'button[name=login]').click()


time.sleep(2)
driver.quit()

