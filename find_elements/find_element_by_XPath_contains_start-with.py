from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# WAP to open eCom site
# and search for cap item
# show usages of contains() and start-with()

driver = webdriver.Firefox()
driver.get('http://localhost/coolsite')
driver.maximize_window()

# search for cap item using contains(), ID = wp-block-search__input-1
driver.find_element(By.XPATH, '//input[contains(@id, "wp-block-search")]').send_keys('cap')

# click on search button using start-with(), ID = wp-block-search__input-1
driver.find_element(By.XPATH, '//button[contains(@class, "wp-block-search__button")]').click()

time.sleep(2)
driver.quit()
