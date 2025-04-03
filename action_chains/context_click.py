"""
This script automates the context click (right-click) Action Chain.

@author: Raed Eleyan.
@date: 04/03/2025.
@contact: raedeleyan1@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://demoqa.com/buttons')
driver.maximize_window()
right_click_button = driver.find_element(By.ID, 'rightClickBtn')
actions = ActionChains(driver)
actions.context_click(right_click_button).perform()
try:
    right_click_message = driver.find_element(By.ID, 'rightClickMessage')
    print('Great! Performed context-click action chain successfully.')
except NoSuchElementException as e:
    print('Unfortunately! did not perform context-click action chain successfully.')
driver.quit()