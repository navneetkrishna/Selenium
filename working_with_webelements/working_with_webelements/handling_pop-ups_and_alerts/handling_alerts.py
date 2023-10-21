import time
from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get('file:///D:/pyc_project/Selenium/working_with_webelements/alerts.html')

btn2 = driver.find_element(By.XPATH, '//button[@id="button2"]')
btn2.click()

# method 1
# alert_popup = driver.switch_to.alert

# method 2
alert_popup = Alert(driver)

print(alert_popup.text)
alert_popup.accept()
# alert_popup.dismiss()
# alert_popup.send_keys('Random')

time.sleep(2)
