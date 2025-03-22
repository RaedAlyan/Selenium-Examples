"""
This script locates a WebElement using WildCards with CSS Selector strategy.

@author: Raed Eleyan.
@date: 03/22/2025.
@contact: raedeleyan1@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://the-internet.herokuapp.com/login')
driver.maximize_window()

# 1- ^: it selects a WebElement that has an attribute value that **starts** with a specific string.
form_input = driver.find_element(By.CSS_SELECTOR, 'form[action^="/auth"]')

# 2- ~: it selects a WebElement where the attribute contains the specified value as a whole word.
divs = driver.find_elements(By.CSS_SELECTOR, 'div[class~="columns"]')

# 3- $: it selects a WebElement where the attribute ends with the specified value.
div_footer = driver.find_element(By.CSS_SELECTOR, 'div[id$="footer"]')

# 4- *: it selects a WebElement where the attribute contains the specified value.
web_element = driver.find_element(By.CSS_SELECTOR, 'i[class*="sign"]')
driver.quit()
