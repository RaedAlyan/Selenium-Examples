"""
This script locates a WebElement using the parent XPath axes.

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
driver.maximize_window()
# locate the parent WebElement of a current parent using the parent axes
div_parent = driver.find_element(By.XPATH, '//label[text()="First Name "]/parent::div')
print(div_parent)
driver.quit()
