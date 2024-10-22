import time

from selenium import webdriver

# Open Browser Chrome use WebDriver
driver = webdriver.Chrome()
time.sleep(2) # Pauses execution for 2 seconds

# Navigate to webpage
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(5) # Pauses execution for 5 seconds