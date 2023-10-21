import time
from selenium import webdriver

optns = webdriver.EdgeOptions()
optns.add_argument('--disable-notifications')
driver = webdriver.Edge(options=optns)

driver.get('https://whatmylocation.com/')

