from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('https://www.google.com/')

# driver will wait for max of 10 sec
# for any driver to load
# if loaded early, execute next line
driver.implicitly_wait(10)

driver.find_element(By.ID, 'APjFqb').send_keys('qwe')


# driver.implicitly_wait(10)                    # no effect
# if declared  here, it will have no effect
# since there are no elements after this line

driver.quit()
