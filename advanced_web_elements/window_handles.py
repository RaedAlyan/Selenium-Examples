"""
This script automates window handles.

@author: Raed Eleyan.
@date: 04/03/2025.
@contact: raedeleyan1@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://the-internet.herokuapp.com/windows')
driver.maximize_window()

# Get current window handle
current_window_handle = driver.current_window_handle
print(f'Current window handle: {current_window_handle}')

# Get all opened window handles
opened_window_handles = driver.window_handles
print(f'Number of opened window handles: {len(opened_window_handles)}, and they are: {opened_window_handles}')

# Click on a button to open a new tab
button = driver.find_element(By.LINK_TEXT, 'Click Here')
button.click()

# Get all opened window handles
opened_window_handles = driver.window_handles
print(f'Number of opened window handles: {len(opened_window_handles)}, and they are: {opened_window_handles}')

# Switch to the new opened tab
driver.switch_to.window(opened_window_handles[-1])

# Get the current header text
header_text = driver.find_element(By.TAG_NAME, 'h3').text

if header_text == 'New Window':
    print('Great! New window has been opened and switched to it successfully.!')
else:
    print('Oops! Something went wrong.')
driver.quit()
