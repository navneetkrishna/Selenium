from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('http://localhost/coolsite/shop')
driver.maximize_window()

time.sleep(2)

# relative XPath and use of 'or' to add album to cart
driver.find_element(By.XPATH, '//a[@data-product_id=44 or @class=add_to_cart_button ]').click()

# # relative XPath and use of 'or 'to add album to cart using wildcard
# driver.find_element(By.XPATH, '//*[@data-product_id=44 or @class=add_to_cart_button ]').click()

time.sleep(3)
# relative XPath and use of 'and' to search for item cap on cart page
driver.find_element(By.XPATH, '//input[@class="wp-block-search__input" and @type="search"]').send_keys('cap')

# relative XPath and use of 'and' to search for item cap on cart page
driver.find_element(By.XPATH, '//button[@class="wp-block-search__button wp-element-button" and @type="submit"]').click()


time.sleep(3)

driver.quit()
