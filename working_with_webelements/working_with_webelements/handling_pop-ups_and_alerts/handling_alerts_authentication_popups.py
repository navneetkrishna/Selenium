import time
from selenium import webdriver

driver = webdriver.Edge()
driver.maximize_window()

# authentication pop-up
# driver.get('https://the-internet.herokuapp.com/basic_auth')

# by-pass authentication pop-up
# username, password = admin
driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')

time.sleep(4)
driver.quit()


