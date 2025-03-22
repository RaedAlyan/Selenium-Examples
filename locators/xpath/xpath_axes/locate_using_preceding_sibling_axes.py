"""
This script locates a WebElement using the preceding-sibling XPath axes.

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
# locate the last name input field using the preceding-sibling axes
last_name_input = driver.find_element(By.XPATH, '//label[text()="Email"]//preceding-sibling::input[@name="name" and @maxlength="15"]')
print(last_name_input)
driver.quit()
