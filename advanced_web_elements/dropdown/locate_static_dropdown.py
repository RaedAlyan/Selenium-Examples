from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://the-internet.herokuapp.com/dropdown')
# 1- locate the dropdown WebElement.
dropdown_web_element = driver.find_element(By.ID, 'dropdown')
# 2- create a Select instance
select = Select(dropdown_web_element)
# select an option using its index
select.select_by_index(0)
# select an option using its visible text
select.select_by_visible_text('Option 1')
# select an option using the value of its value attribute
select.select_by_value('1')
driver.quit()
