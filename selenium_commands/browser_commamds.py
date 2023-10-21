from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('http://localhost/coolsite')
driver.maximize_window()

driver.find_element(By.XPATH, "//a[contains(text(),'Built with Storefront & WooCommerce')]").click()

# close() will close the parent URL
# but the browser will be running
driver.close()

time.sleep(2)
# to quit entire process/browser
driver.quit()
