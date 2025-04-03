"""
This script automates the click Action Chain.

@author: Raed Eleyan.
@date: 04/03/2025.
@contact: raedeleyan1@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.maximize_window()
radio_button_element = driver.find_element(By.ID, 'inlineRadio2')
# initiate an object from ActionChains class
actions = ActionChains(driver)
# Perform click action chain
actions.click(radio_button_element).perform()
driver.quit()
