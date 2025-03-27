from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.maximize_window()
# declare implicit waits
driver.implicitly_wait(5)
input_search = driver.find_element(By.CSS_SELECTOR, 'input[class="search-keyword"]')
input_search.send_keys('Tomato')
search_button = driver.find_element(By.CSS_SELECTOR, 'button[class="search-button"]')
search_button.click()
driver.quit()
