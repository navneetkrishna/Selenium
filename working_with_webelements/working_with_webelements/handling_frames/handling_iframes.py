import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get('https://demo.automationtesting.in/Frames.html')


# single frame example
# id = singleframe
driver.switch_to.frame('singleframe')
driver.find_element(By.XPATH, '/html/body/section/div/div/div/input').send_keys('Hi')


# returning focus to the web page
driver.switch_to.default_content()

time.sleep(3)

# -----------------
# inner frame example
driver.find_element(By.LINK_TEXT, 'Iframe with in an Iframe').click()


time.sleep(3)

