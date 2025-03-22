"""
This script locates a WebElement using the Class Name strategy.

@author: Raed Eleyan.
@date: 03/22/2025.
@contact: raedeleyan1@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


webdriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
webdriver.get('https://the-internet.herokuapp.com/login')
login_button = webdriver.find_element(By.CLASS_NAME, 'radius')
webdriver.quit()
