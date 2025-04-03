from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()
check_box = driver.find_element(By.ID, 'checkBoxOption1')
actions = ActionChains(driver)
actions.double_click(check_box).perform()
if check_box.is_selected():
    print('Selected! Did not perform double click action chain successfully.')
else:
    print('Unselected! Performed double click action chain successfully.')
driver.quit()
