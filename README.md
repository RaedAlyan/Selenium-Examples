# Selenium Examples

This repo contains different examples that are implemented using Selenium.

# Key Features:

## Cross-Browser Automation
- The examples demonstrate how to initialize different WebDrivers, including:
  - **ChromeDriver** for Google Chrome
  - **GeckoDriver** for Mozilla Firefox
  - **EdgeDriver** for Microsoft Edge

## WebDriver Manager
- The examples use **WebDriver Manager** library to automatically downloads and configures the appropriate WebDrivers.
- You can install WebDriver Manager using `pip`. Run the following command in your terminal:
```bash
  pip install webdriver-manager
```

## Locators Used
- In this repository, various types of locators are demonstrated to interact with web elements. Below is a list of the locators used:

### 1. **Basic Locators**
   - **ID**: Locates an element by its `id` attribute.
     ```python
     driver.find_element(By.ID, "element-id")
     ```
   - **Class Name**: Locates an element by its `class` attribute.
     ```python
     driver.find_element(By.CLASS_NAME, "element-class")
     ```
   - **Name**: Locates an element by its `name` attribute.
     ```python
     driver.find_element(By.NAME, "element-name")
     ```
   - **Tag Name**: Locates an element by its HTML tag name.
     ```python
     driver.find_element(By.TAG_NAME, "div")
     ```
   - **Link Text**: Locates a link by its exact text.
     ```python
     driver.find_element(By.LINK_TEXT, "Click Here")
     ```
   - **Partial Link Text**: Locates a link by a substring of its text.
     ```python
     driver.find_element(By.PARTIAL_LINK_TEXT, "Click")
     ```

### 2. **CSS Selectors**
   - **ID**: Locates an element using the `#` symbol.
     ```python
     driver.find_element(By.CSS_SELECTOR, "#element-id")
     ```
   - **Class Name**: Locates an element using the `.` symbol.
     ```python
     driver.find_element(By.CSS_SELECTOR, ".element-class")
     ```
   - **Single Attribute**: Locates an element using an attribute.
     ```python
     driver.find_element(By.CSS_SELECTOR, "input[type='text']")
     ```
   - **Multiple Attributes**: Combines multiple attributes for precise targeting.
     ```python
     driver.find_element(By.CSS_SELECTOR, "input[type='text'][name='username']")
     ```
   - **Wildcards**:
     - `*`: Matches elements where the attribute contains a specific substring.
       ```python
       driver.find_element(By.CSS_SELECTOR, "input[name*='user']")
       ```
     - `^`: Matches elements where the attribute starts with a specific substring.
       ```python
       driver.find_element(By.CSS_SELECTOR, "input[name^='user']")
       ```
     - `$`: Matches elements where the attribute ends with a specific substring.
       ```python
       driver.find_element(By.CSS_SELECTOR, "input[name$='name']")
       ```
     - `~`: Matches elements where the attribute contains a specific word.
       ```python
       driver.find_element(By.CSS_SELECTOR, "input[class~='button']")
       ```

### 3. **XPath**
   - **Relative XPath**: Locates an element relative to another element.
     ```python
     driver.find_element(By.XPATH, "//div[@id='container']//input")
     ```
   - **Absolute XPath**: Locates an element using the full path from the root.
     ```python
     driver.find_element(By.XPATH, "/html/body/div/input")
     ```
   - **XPath Axes**: Uses axes like `parent`, `child`, `ancestor`, etc., for navigation.
     ```python
     driver.find_element(By.XPATH, "//div[@id='container']/child::input")
     ```
   - **XPath Functions**: Uses functions like `contains()`, `starts-with()`, and `text()`.
     ```python
     driver.find_element(By.XPATH, "//div[contains(@class, 'example')]")
     ```

## Advanced Web Elements
- This repo includes examples of handling advanced web elements, such as:
### 1. Dropdowns
- **Dropdowns** are commonly used in web applications for selecting options.
- There are two types of dropdowns:
  - **Static Dropdown**:
    - it's created using the `<select>` tag, and we **can** interact with it using `Select` class.
  - **Dynamic Dropdown**:
    - it's not created using the `<select>` tag, and we **can't** interact with it using 'Select' class.
    - To interact with dynamic dropdown:
      - Locate the dynamic dropdown.
      - Click on (or type something) the dynamic dropdown to expand it.
      - Wait for options to load.
      - Locate and click the desired option.
### 2. Checkboxes
- **Checkboxes** allow users to select one or multiple choices from a set.
### 3. Radio Button
- **Radio button** allow users to select only one option from a set.
### 4. Alert popup
- **Alert popup** isn't part of the DOM, and Selenium can't locate it using locators.
- To interact with alert popup, we need to switch to it and perform required actions such as `accept()`, `dismiss()`, `text`, and `send_keys()`.
- We can switch to an alert popup using this command:
    ```python
    alert = driver.switch_to.alert
    ```
## Synchronization
- Selenium provides three wait strategies:
### 1. Implicit Wait
- Implicit wait is a syn technique that allows to pause test execution for a certain amount of time before throwing a NoSuchElementException if the element isn’t found.
### 2. Explicit Wait
- Explicit wait is a sync technique that allows to pause test execution until a specific condition is met or a timeout is reached.
### 3. Fluent Wait
- Fluent wait is an advanced sync technique that provides flexible, customizable waiting for elements with: configurable max timeout, adjustable polling frequency, ability to ignore specific conditions, and custom wait conditions.

## Action Chains
- **Action Chains** are a powerful feature in Selenium that automates and handles complex user interactions.
- This repo automates some common action chains such as: click, double-click, context-click, hover-over-element, and drag-and-drop Action Chains.

## Window Handles
- Window Handles allows to work with multiple browser windows or tabs.
