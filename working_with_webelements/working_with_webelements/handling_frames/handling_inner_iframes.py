from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get('https://demo.automationtesting.in/Frames.html')

# click on the toggle button to get th inner frame example
driver.find_element(By.LINK_TEXT, 'Iframe with in an Iframe').click()

# since frames does not have name, ID
# create a web element for outer frame
outer_frame = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")

# switch focus to outer frame
driver.switch_to.frame(outer_frame)

# create a web element for inner frame
inner_frame = driver.find_element(By.XPATH, "//iframe[contains(text(),'<p>Your browser does not support iframes.</p>')]")

# switch focus to outer frame
driver.switch_to.frame(inner_frame)

driver.find_element(By.XPATH, "//input[@type='text']").send_keys('hi')

# switch to parent/outer frame
driver.switch_to.parent_frame()

time.sleep(1)
driver.quit()
