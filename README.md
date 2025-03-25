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
