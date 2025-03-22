"""
This script locates a WebElement using the following-sibling XPath axes.

@author: Raed Eleyan.
@date: 03/22/2025.
@contact: raedeleyan1@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

webdriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
webdriver.get('https://www.hyrtutorials.com/p/add-padding-to-containers.html')
# locate the email input field using the following-sibling axes
email_input = webdriver.find_element(By.XPATH, '//label[text()="Email"]/following-sibling::input[@type="text"]')
print(email_input)
webdriver.quit()
