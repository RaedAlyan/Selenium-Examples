"""
This script locates a WebElement using the relative XPath.

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
# locate the login button using the relative xpath
login_button = driver.find_element(By.XPATH, '//button[@class="radius"]')
print(login_button.text)
driver.quit()
