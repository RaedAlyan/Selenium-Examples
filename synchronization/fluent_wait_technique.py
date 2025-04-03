"""
This script automates handling fluent wait technique.

@author: Raed Eleyan.
@date: 04/03/2025.
@contact: raedeleyan1@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ScreenshotException

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.maximize_window()
# fluent wait until the element becomes visible
input_search = WebDriverWait(driver, timeout=10, poll_frequency=2, ignored_exceptions=[ScreenshotException]).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[class="search-keyword"]'))
)
input_search.send_keys('Tomato')
# fluent wait until the element becomes clickable
search_button = WebDriverWait(driver, timeout=10, poll_frequency=2, ignored_exceptions=[ScreenshotException]).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[class="search-button"]'))
)
search_button.click()
driver.quit()
