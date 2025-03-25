from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://the-internet.herokuapp.com/checkboxes')
driver.maximize_window()
checkbox_element = driver.find_element(By.XPATH, '//form/child::input[1]')
checkbox_element.click()
if checkbox_element.is_selected():
    print('The checkbox is selected.')
else:
    print('The checkbox is not selected.')
    checkbox_element.click()
driver.quit()
