"""
This script locates a WebElement using the following XPath axes.

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
# locate all following div WebElements using the following axes
div_elements = driver.find_elements(By.XPATH, '//div[@class="container"]/following::div')
print(len(div_elements))
driver.quit()
