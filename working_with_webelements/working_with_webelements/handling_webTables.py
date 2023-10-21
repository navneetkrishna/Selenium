# Objectives
# 1. Count the number of rows and columns
# 2. Read specific row and column and data
# 3. Read all the rows and column data
# 4. Read data based on conditions (List of email where due amount is > 50)
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get('https://the-internet.herokuapp.com/tables')

# 1. Count the number of rows and columns

#  total column = number of elements in table head
columns = driver.find_elements(By.XPATH, "//table[@id='table1']//th")
print('total number of columns: ' + str(len(columns)))


# total rows = total <tr> tags
rows = driver.find_elements(By.XPATH, "//table[@id='table1']/tbody/tr")
print('total number of rows: ' + str(len(rows)))
print(rows[0].text)


# 2. Read specific row and column and data - 'jdoe@hotmail.com'
print(driver.find_element(By.XPATH, "//table[@id='table1']/tbody/tr[3]/td[3]").text)


# 3. Read all the rows and column data
# approach 1
for r in range(1, len(rows)+1):
    for c in range(1, len(columns)+1):
        # print('r: ', r, 'c: ', c, end='     ')
        print(driver.find_element(By.XPATH, "//table[@id='table1']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text, end='   ')

    print()


#  approach 2
# for column in columns:
#     print(column.text + '\t', end='    ')
#
# for row in rows:
#     print(row.text + '\t', end='    ')
#     print()


# 4. Read data based on conditions (Email where first name is Frank)
for r in range(1, len(rows)+1):
    name = driver.find_element(By.XPATH, "//table[@id='table1']/tbody/tr[" + str(r) + "]/td[2]").text
    if name == 'Frank':
        print(driver.find_element(By.XPATH, "//table[@id='table1']/tbody/tr[" + str(r) + "]/td[3]").text)

time.sleep(2)
