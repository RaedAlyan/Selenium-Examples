"""
This script handles Edge browser options.

@author: Raed Eleyan.
@date: 04/05/2025.
@contact: raedeleyan1@gmail.com
"""
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

edge_options = Options()
# Common Edge options
edge_options.add_argument("--start-maximized")
edge_options.add_argument("--inprivate")  # InPrivate mode
edge_options.add_argument("--headless")
edge_options.add_argument("--disable-notifications")

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)
driver.get('https://www.google.com/')
driver.quit()
