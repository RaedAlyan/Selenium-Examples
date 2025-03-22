"""
This script locates a WebElement using the Single Attribute CSS Selector strategy.

@author: Raed Eleyan.
@date: 03/22/2025.
@contact: raedeleyan1@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://the-internet.herokuapp.com/login')
driver.maximize_window()
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
driver.quit()
