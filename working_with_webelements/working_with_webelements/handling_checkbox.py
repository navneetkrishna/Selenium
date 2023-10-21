import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Specify the path to the Chrome WebDriver executable
driver = webdriver.Firefox()

# Navigate to the target web page and maximize the window
driver.get('file:///D:/pyc_project/Selenium/working_with_webelements/weekdays_checkboxes.html')
driver.maximize_window()

# Find all the checkboxes on the page
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(f"Number of checkboxes found: {len(checkboxes)}")

# Uncomment and use the desired approach:

# Approach 1: Select a specific checkbox by ID
driver.find_element(By.XPATH, "//input[@id='monday']").click()

# Approach 2: Select all checkboxes
for checkbox in checkboxes:
    checkbox.click()

# Approach 3: Select specific checkboxes by choice (e.g., Monday and Sunday)
for checkbox in checkboxes:
    week_name = checkbox.get_attribute('id')
    if week_name == 'monday' or week_name == 'sunday':
        checkbox.click()

# Approach 4: Select the last 2 checkboxes
for i in range(len(checkboxes) - 2, len(checkboxes)):
    checkboxes[i].click()

# Approach 5: Select the first 2 checkboxes
for i in range(len(checkboxes)):
    if i < 2:
        checkboxes[i].click()

# Approach 6: Clear all checkboxes (deselect all)
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()

# Close the WebDriver
driver.quit()
