# https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true

import time

from selenium.webdriver.support.select import Select
from Selenium.data_driven_testing import excel_util
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get('https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true')
driver.maximize_window()

cwd = os.getcwd()
file = cwd+'\\FD_interest_cal.xlsx'
# print(file)

max_row = excel_util.get_row_count(file, 'Sheet1')
max_col = excel_util.get_col_count(file, 'Sheet1')
# print(f'Total rows: {max_row} total columns: {max_col}')

for r in range(2, max_row+1):
    principal_amt = excel_util.read_data(file, 'Sheet1', r, 1)
    roi = excel_util.read_data(file, 'Sheet1', r, 2)
    tenure = excel_util.read_data(file, 'Sheet1', r, 3)
    tenure_period = excel_util.read_data(file, 'Sheet1', r, 4)
    frequency = excel_util.read_data(file, 'Sheet1', r, 5)
    expected_result = '{:.2f}'.format(float(excel_util.read_data(file, 'Sheet1', r, 6)))

    # print(principal_amt, roi, tenure, tenure_period, frequency)

    # Enter principal amount
    principal_amt_element = driver.find_element(By.XPATH,'//input[@id="principal"]')
    principal_amt_element.send_keys(principal_amt)

    # Enter roi
    roi_element = driver.find_element(By.XPATH,'//input[@id="interest"]')
    roi_element.send_keys(roi)

    # Enter tenure
    tenure_element = driver.find_element(By.XPATH, '//input[@id="tenure"]')
    tenure_element.send_keys(tenure)

    # Select tenure period
    Select(driver.find_element(By.XPATH, '//select[@id="tenurePeriod"]')).select_by_visible_text(tenure_period)

    # Select frequency
    Select(driver.find_element(By.XPATH, '//select[@id="frequency"]')).select_by_visible_text(frequency)

    # click on calculate button
    image_button = driver.find_element(By.XPATH, "//body//div[@class='CTR PT15']/a[1]")
    driver.execute_script("arguments[0].click();", image_button)

    result = driver.find_element(By.XPATH, '//span[@id="resp_matval"]').text

    # print(type(result), type(expected_result))
    # print(result, expected_result)
    if result == expected_result:
        print('pass')
        excel_util.write_data(file, 'Sheet1', r, 7, 'Pass')
    else:
        print('fail')
        excel_util.write_data(file, 'Sheet1', r, 7, 'Fail')

    # clear all text boxes
    principal_amt_element.clear()
    roi_element.clear()
    tenure_element.clear()

    # time.sleep(5)



