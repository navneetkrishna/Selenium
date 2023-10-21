from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('http://localhost/coolsite')
driver.maximize_window()

driver.find_element(By.XPATH, "//ul[@class='nav-menu']//li[@class='page_item page-item-9']//a[contains(text(),"
                              "'My account')]").click()
time.sleep(2)
driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()

driver.quit()
