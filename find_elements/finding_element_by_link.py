from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get('http://localhost/coolsite')

cart = driver.find_element(By.LINK_TEXT, 'Cart')
cart.click()

footer_link_text = driver.find_element(By.PARTIAL_LINK_TEXT, 'Built with Storefro')
print(footer_link_text.text)

driver.quit()
