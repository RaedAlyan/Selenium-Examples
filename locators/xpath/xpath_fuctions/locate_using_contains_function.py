"""
This script locates a WebElement using the contains() XPath function.

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
# locate a WebElement using the contains function
web_element = driver.find_element(By.XPATH, '//div[contains(@id, "footer")]')
print(web_element.text)
driver.quit()
