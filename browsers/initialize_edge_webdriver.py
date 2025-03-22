"""
This script initializes the Edge WebDriver using WebDriver Manager and Python.

@author: Raed Eleyan.
@date: 03/22/2025.
@contact: raedeleyan1@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# Initializes the Edge WebDriver
driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
# Navigates to Google website.
driver.get('https://www.google.com')
# Maximizes window.
driver.maximize_window()
# Quits the WebDriver session
driver.quit()
