"""
This script automates the move-to-element (Hovers-over-element) Action Chain.

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
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
mouse_hover_element = driver.find_element(By.ID, 'mousehover')
actions = ActionChains(driver)
actions.move_to_element(mouse_hover_element).perform()
mouse_hover_contents = driver.find_elements(By.XPATH, '//div[@class="mouse-hover-content"]/child::a')
if len(mouse_hover_contents) > 0:
    print('Great! Performed move-to-element action chain successfully.')
    for content in mouse_hover_contents:
        print(content.text)
else:
    print('Unfortunately! Did not perform move-to-element action chain successfully.')
driver.quit()
