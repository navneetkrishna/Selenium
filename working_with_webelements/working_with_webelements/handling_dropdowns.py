import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Edge()
driver.get('file:///D:/pyc_project/Selenium/working_with_webelements/demoHTML.html')

my_wait = WebDriverWait(driver, 100, ignored_exceptions=[NoSuchElementException])

# get the dropdown web element
# dropdown element has 'select' tag

# cntry_dropdown = driver.find_element(By.XPATH, '//select[@id="input-country"]')
cars_dropdown = my_wait.until(EC.presence_of_element_located((By.XPATH, '//select[@id="cars"]')))

# create object of Select class by passing dropdown
# var. will contain all the options available
options_webElement = Select(cars_dropdown)

# select one option 'Saab'
options_webElement.select_by_visible_text('Saab')
# options_webElement.deselect_by_value('mercedes')
# options_webElement.select_by_index(3)

# capture all the options from the dropdown
option_list = options_webElement.options

for option in option_list:
    print(option.text)

# Select the option 'Mercedes' without using built-in function
for option in option_list:
    if option.text == 'Mercedes':
        option.click()
        break                   # break as the condition meets


time.sleep(2)



