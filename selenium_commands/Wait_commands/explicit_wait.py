from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get('https://www.google.com/')

# my_wait = WebDriverWait(driver, 10)        # explicit wait declaration basic
# my_wait = WebDriverWait(driver, 10, ignored_exceptions=[Exception])
my_wait = WebDriverWait(driver, 10, ignored_exceptions=[NoSuchElementException])


# search for Selenium
# and click on first link
search_box = driver.find_element(By.ID, 'APjFqb')
search_box.send_keys('Selenium')
search_box.submit()

sel_link = my_wait.until(EC.presence_of_element_located((By.XPATH, "//div[@lang='en']//div[@class='tF2Cxc']//div[@class='yuRUbf']//div//span[@jscontroller='msmzHf']//a[@jsname='UWckNb']//h3[@class='LC20lb MBeuO DKV0Md'][contains(text(),'Selenium')]")))
sel_link.click()

driver.quit()
