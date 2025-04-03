"""
This script automates handling dynamic dropdown WebElement.

@author: Raed Eleyan.
@date: 04/03/2025.
@contact: raedeleyan1@gmail.com
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://rahulshettyacademy.com/dropdownsPractise/')
driver.maximize_window()
# locate the dropdown WebElement.
dropdown = driver.find_element(By.ID, 'autosuggest')
# Send some keys to the dropdown WebElement.
dropdown.send_keys('ind')
# Wait for options to be loaded.
time.sleep(2)
# locate the link option that contains Australia as its visible text.
desired_options = driver.find_elements(By.XPATH, '//li[@class="ui-menu-item"]/child::a')
# Select the desired option
for option in desired_options:
    if option.text == 'India':
        option.click()
        break
driver.quit()
