"""
This script locates a WebElement using the starts-with() XPath function.

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
# locate a WebElement using the starts-with() function
web_element = driver.find_element(By.XPATH, '//div[starts-with(@id, "page")]')
print(web_element.text)
driver.quit()
