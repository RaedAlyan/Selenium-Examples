"""
This script automates handling IFrames.

@author: Raed Eleyan.
@date: 04/03/2025.
@contact: raedeleyan1@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
# Locate IFrame WebElement
iframe_element = driver.find_element(By.ID, 'courses-iframe')
# Switch to the IFrame
driver.switch_to.frame(iframe_element)
# Locate a WebElement within the IFrame
register_button = driver.find_element(By.XPATH, '//div[@class="login-btn"]/child::a[text()="Register"]')
# Click on the button that is located inside the IFrame.
register_button.click()
# Switch back to the parent frame
driver.switch_to.default_content()
driver.quit()
