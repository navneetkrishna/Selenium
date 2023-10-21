from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('http://localhost/coolsite')
driver.maximize_window()

search_box = driver.find_element(By.XPATH, "//input[@id='woocommerce-product-search-field-0']")
print(search_box.is_displayed())
print(search_box.is_enabled())

# is_selected
# browse to my account page
driver.find_element(By.XPATH, "//ul[@class='nav-menu']//li[@class='page_item page-item-9']//a[contains(text(),"
                              "'My account')]").click()

remember_me = driver.find_element(By.XPATH, "//input[@id='rememberme']")
print(remember_me.is_selected())


time.sleep(1)
driver.quit()
