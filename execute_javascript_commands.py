from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.maximize_window()

# Execute a JS command to make a popup message
driver.execute_script("alert('Hello from Selenium!');")

button_element = driver.find_element(By.CSS_SELECTOR, 'input[value="radio1"]')
# Click an element
driver.execute_script("arguments[0].click();", button_element)
driver.quit()
