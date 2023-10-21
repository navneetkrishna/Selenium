from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.get('https://money.rediff.com/gainers')
driver.maximize_window()

# self
self = driver.find_element(By.XPATH,"//a[contains(text(),'Kush Industries')]/self::a").text
print(self)             # Kush Industries

# parent
parent = driver.find_element(By.XPATH, "//a[contains(text(),'Kush Industries')]/parent::td").text
print(parent)           # Kush Industries

# child
children = driver.find_elements(By.XPATH,"//a[contains(text(),'Kush Industries')]/ancestor::tr/child::td")
print(len(children))    # 5


# Ancestor
ancestor = driver.find_element(By.XPATH,"//a[contains(text(),'Kush Industries')]/ancestor::tr").text
print(ancestor)         # Kush Industries A 358.35 375.30 + 4.73


# Descendant
descendants = driver.find_elements(By.XPATH,"//a[contains(text(),'Kush Industries')]/ancestor::tr/descendant::*")
print("Number of descendant nodes:",len(descendants))       # 7


# Following
followings = driver.find_elements(By.XPATH,"//a[contains(text(),'Kush Industries')]/ancestor::tr/following::*")
print("Number of descendant nodes:",len(followings))        # 719


# Following-sibling
following_siblings = driver.find_elements(By.XPATH, "//a[contains(text(),'Kush Industries')]/ancestor::tr/following-sibling::*")
print("Number of descendant nodes:", len(following_siblings))   # 72


# preceding
preceding = driver.find_elements(By.XPATH,"//a[contains(text(),'India Tourism De')]/ancestor::tr/preceding::*")
print(len(preceding))               # 251


# preceding-sibling
preceding_siblings = driver.find_elements(By.XPATH, "//a[contains(text(),'Kush Industries')]/ancestor::tr/preceding-sibling::tr")
print(len(preceding_siblings))      # 11


driver.quit()
