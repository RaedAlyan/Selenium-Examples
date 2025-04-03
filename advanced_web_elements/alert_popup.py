"""
This script automates handling alert-popup messages.

@author: Raed Eleyan.
@date: 04/03/2025.
@contact: raedeleyan1@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
name_input = driver.find_element(By.ID, 'name')
name_input.send_keys('Raed')
confirm_button = driver.find_element(By.ID, 'confirmbtn')
confirm_button.click()
# switch to the alert popup
alert = driver.switch_to.alert
print(alert.text)
# to click on Ok button
alert.accept()
# to click on cancel button
# alert.dismiss()
driver.quit()
