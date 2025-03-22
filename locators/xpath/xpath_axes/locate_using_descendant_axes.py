"""
This script locates a WebElement using the descendant XPath axes.

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
# locate the Password label using the descendant axes
password_label = driver.find_element(By.XPATH, '//div[@class="container"]/descendant::label[text()="Password"]')
print(password_label.text)
driver.quit()
