"""
This script locates a WebElement using the ancestor XPath axes.

@author: Raed Eleyan.
@date: 03/22/2025.
@contact: raedeleyan1@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.hyrtutorials.com/p/add-padding-to-containers.html')
# locate the form WebElement using the ancestor axes
form_web_element = driver.find_element(By.XPATH, '//label[text()="Email"]//ancestor::form')
driver.quit()
