"""
This script handles Firefox browser options.

@author: Raed Eleyan.
@date: 04/05/2025.
@contact: raedeleyan1@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


firefox_options = Options()
# Common Firefox options
firefox_options.add_argument("--start-maximized")
firefox_options.add_argument("--headless")
firefox_options.add_argument("--disable-notifications")

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)
driver.get("https://www.google.com")
driver.quit()
