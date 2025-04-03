"""
This script automates the drag-and-drop Action Chain.

@author: Raed Eleyan.
@date: 04/03/2025.
@contact: raedeleyan1@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://the-internet.herokuapp.com/drag_and_drop')
driver.maximize_window()
source_element = driver.find_element(By.ID, 'column-a')
target_element = driver.find_element(By.ID, 'column-b')
actions = ActionChains(driver)
actions.drag_and_drop(source_element, target_element).perform()
source_element_text = driver.find_element(By.XPATH, '//div[@id="columns"]/descendant::header[1]').text
if source_element_text == 'B':
    print('Great! Performed drag-and-drop action chain successfully.')
else:
    print('Unfortunately! Did not perform drag-and-drop action chain successfully.')
driver.quit()
