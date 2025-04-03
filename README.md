# Selenium Examples

A comprehensive collection of Selenium WebDriver implementations demonstrating best practices for web automation testing.

## 🚀 Key Features

### 🌐 Cross-Browser Support
Examples for initializing and automating different browsers:
- **Chrome** using `ChromeDriver`
- **Firefox** using `GeckoDriver` 
- **Edge** using `EdgeDriver`

### ⚙️ WebDriver Manager Integration
Automate browser driver management with the `webdriver-manager` package, eliminating manual driver downloads and version mismatches.
#### Installation
```bash
  pip install webdriver-manager
```

## 🔍 Element Location Strategies
```python
# ===== BASIC LOCATORS =====
# By ID: Locates an element by its id attribute.
driver.find_element(By.ID, "element-id")

# By Class Name: Locates an element by its class attribute.
driver.find_element(By.CLASS_NAME, "element-class")

# By Name: Locates an element by its name attribute.
driver.find_element(By.NAME, "element-name")

# By Tag Name: Locates an element by its HTML tag name.
driver.find_element(By.TAG_NAME, "html-tag-name")

# By Link Text: Locates a link by its exact text.
driver.find_element(By.LINK_TEXT, "Click Here")

# By Partial Link Text: Locates a link by a substring of its text.
driver.find_element(By.PARTIAL_LINK_TEXT, "Click")


# ===== CSS SELECTORS =====
# ID selector: Locates an element using the `#` symbol.
driver.find_element(By.CSS_SELECTOR, "#element-id")

# Class selector: Locates an element using the `.` symbol.
driver.find_element(By.CSS_SELECTOR, ".element-class")

# Attribute selector: Locates an element using an attribute
driver.find_element(By.CSS_SELECTOR, "input[type='text']")

# Multiple attributes: Combines multiple attributes for precise targeting.
driver.find_element(By.CSS_SELECTOR, "input[type='text'][name='username']")

# Wildcards
driver.find_element(By.CSS_SELECTOR, "input[name*='user']") # Matches elements where the attribute contains a specific substring.
driver.find_element(By.CSS_SELECTOR, "input[name^='user']") # Matches elements where the attribute starts with a specific substring.
driver.find_element(By.CSS_SELECTOR, "input[name$='name']") # Matches elements where the attribute ends with a specific substring.
driver.find_element(By.CSS_SELECTOR, "input[class~='button']") # Matches elements where the attribute contains a specific word.


# ===== XPATH LOCATORS =====
# Absolute path: Locates an element using the full path from the root.
driver.find_element(By.XPATH, "/html/body/div/input")

# Relative path: Locates an element relative to another element.
driver.find_element(By.XPATH, "//div[@id='container']//input")

# Using functions: Uses functions like contains(), starts-with(), and text().
driver.find_element(By.XPATH, "//div[contains(@class, 'example')]")

# Logical operators
driver.find_element(By.XPATH, "//input[@type='text' and @name='email']")

# XPath Axes: Uses axes like parent, child, ancestor, etc., for navigation.
driver.find_element(By.XPATH, "//div[@id='container']/child::input")
```

## 🧩 Web Component Handling
```python
# ===== DROPDOWNS =====
# Static dropdowns (<select> tag)
from selenium.webdriver.support.ui import Select

dropdown = Select(driver.find_element(By.ID, "country-dropdown"))
dropdown.select_by_visible_text("Canada")  # Select by text
dropdown.select_by_value("ca")            # Select by value attribute
dropdown.select_by_index(2)               # Select by index (0-based)

# Dynamic dropdowns (custom implementations)
driver.find_element(By.ID, "dropdown-trigger").click()  # Open dropdown
driver.find_element(By.XPATH, "//li[text()='Option 2']").click()  # Select option


# ===== CHECKBOXES =====
checkbox = driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']")

# Check if selected
if not checkbox.is_selected():
    checkbox.click()  # Toggle on

# Uncheck if needed
if checkbox.is_selected():
    checkbox.click()  # Toggle off


# ===== RADIO BUTTONS =====
# Select radio button by value
driver.find_element(By.CSS_SELECTOR, "input[type='radio'][value='option1']").click()

# Verify selection state
radio_button = driver.find_element(By.ID, "radio-option")
print(f"Radio selected: {radio_button.is_selected()}")


# ===== ALERTS/POPUPS =====
# Switch to alert
alert = driver.switch_to.alert

# Get alert text
alert_text = alert.text
print(f"Alert says: {alert_text}")

# Handle alert
alert.accept()    # Click OK
# OR
alert.dismiss()   # Click Cancel

# For prompts (input fields)
alert.send_keys("Sample text")  # Type into prompt
alert.accept()
```

## ⏱ Synchronization Strategies
```python
# ===== IMPLICIT WAIT =====
# Global setting - applies to all find_element calls
driver.implicitly_wait(10)  # Wait up to 10 seconds


# ===== EXPLICIT WAIT =====
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Basic element visibility wait
element = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "dynamic-element"))
)


# ===== FLUENT WAIT =====
# Advanced explicit wait with custom polling/ignores
from selenium.common.exceptions import NoSuchElementException

wait = WebDriverWait(
    driver,
    timeout=30,           # Max wait (seconds)
    poll_frequency=2,     # Check every 2 seconds
    ignored_exceptions=[NoSuchElementException]  # Ignore during polling
)
```

## 🎮 Advanced Interactions
```python
# ===== ACTION CHAINS =====
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

actions = ActionChains(driver)

# Mouse hover + click
actions.move_to_element(menu).click(hidden_submenu).perform()

# Drag and drop
actions.drag_and_drop(source_element, target_element).perform()


# ===== WINDOW HANDLES =====
main_window = driver.current_window_handle

# Open new window
driver.execute_script("window.open('');")

# Switch to new window (last in handle list)
driver.switch_to.window(driver.window_handles[-1])

# Do operations in new window
driver.get("https://example.com")

# Close and return to main
driver.close()
driver.switch_to.window(main_window)
```
