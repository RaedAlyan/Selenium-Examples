from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://rahulshettyacademy.com/angularpractice/')
driver.maximize_window()
radio_button = driver.find_element(By.ID, 'inlineRadio1')
radio_button.click()
if radio_button.is_selected():
    print('Radio button 1 selected successfully')
else:
    print('Radio button 1 not selected')
driver.quit()
