import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('file:///D:/pyc_project/Selenium/working_with_webelements/link_demo_html.html')

driver.find_element(By.XPATH, "//a[contains(text(),'External Link (Google)')]").click()

# ID of the current window
# current_window_ID = driver.current_window_handle

# getting list of IDs of all the windows open
window_IDs = driver.window_handles

# switching to windows
driver.switch_to.window(window_IDs[0])
time.sleep(2)
driver.switch_to.window(window_IDs[1])

print(window_IDs[0])
print(window_IDs[1])
print(driver.current_window_handle)
print(driver.current_window_handle == window_IDs[0])
time.sleep(2)
