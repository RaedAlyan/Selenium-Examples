"""
This script initializes the FireFox WebDriver using WebDriver Manager and Python.

@author: Raed Eleyan.
@date: 03/22/2025.
@contact: raedeleyan1@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Initializes the Firefox WebDriver
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
# Navigates to the Google website.
driver.get('https://www.google.com')
# Maximizes the window.
driver.maximize_window()
# Quits the WebDriver session.
driver.quit()
