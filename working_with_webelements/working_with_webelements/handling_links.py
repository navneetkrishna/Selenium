import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
# driver.get('file:///D:/pyc_project/Selenium/working_with_webelements/link_demo_html.html')
driver.get('http://www.deadlinkcity.com/')

count = 0
all_links = driver.find_elements(By.TAG_NAME, 'a')

for link in all_links:
    url = link.get_attribute('href')  # get the url of each link

    try:
        response = requests.head(url)

        if response.status_code >= 400:
            print('Broken link: ', url)
            count = + 1

        else:
            print('Valid link: ', url)

    except Exception as e:
        print(e)

print('Total broken links: ', count)
