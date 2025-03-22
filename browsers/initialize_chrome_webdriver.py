"""
This script initializes the Chrome webdriver using WebDriver Manager and Python.

@author: Raed Eleyan.
@date: 03/22/2025.
@contact: raedeleyan1@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initializes the chrome WebDriver.
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Navigates to Google website.
driver.get('https://www.google.com')
# Maximizes the window
driver.maximize_window()
# Quits the WebDriver session.
driver.quit()
