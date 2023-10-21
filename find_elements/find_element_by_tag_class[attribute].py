from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('http://localhost/coolsite/shop')
driver.maximize_window()

time.sleep(2)

# sending values to first search field
driver.find_element(By.CSS_SELECTOR, 'input.search-field[name=s]').send_keys('abc')

time.sleep(2)
# sending values to second search field
driver.find_element(By.CSS_SELECTOR, 'input.wp-block-search__input[name=s]').send_keys('def')

time.sleep(2)
driver.quit()

