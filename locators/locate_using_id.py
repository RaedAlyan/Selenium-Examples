"""
This script locates a WebElement using the ID strategy.

@author: Raed Eleyan.
@date: 03/22/2025.
@contact: raedeleyan1@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/login")
driver.maximize_window()
user_name_input = driver.find_element(By.ID, 'username')
password_input = driver.find_element(By.ID, 'password')
driver.quit()
