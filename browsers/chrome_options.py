"""
This script handles Chrome browser options.

@author: Raed Eleyan.
@date: 04/04/2025.
@contact: raedeleyan1@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()

# Common Chrome options
chrome_options.add_argument("--start-maximized")  # Start maximized
chrome_options.add_argument("--incognito")  # Incognito mode
chrome_options.add_argument("--headless")  # Headless mode
chrome_options.add_argument("--disable-notifications")  # Disable notifications
chrome_options.add_argument("--disable-extensions")  # Disable extensions
chrome_options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
chrome_options.add_argument("--no-sandbox")  # Bypass OS security model
chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://www.google.com")
driver.quit()
