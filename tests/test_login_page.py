import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestPositiveScenarios:

    @pytest.mark.login #for selection execute testing
    @pytest.mark.positive
    def test_positive_login(self, driver):
        # Go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(5)  # Pauses execution for 5 seconds

        # Type username student into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("student")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        # Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_button_locator.click()
        time.sleep(2)

        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        actual_url = driver.current_url
        # Make comparison to TRUE
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        text_locator = driver.find_element(By.TAG_NAME, "h1")
        actual_text = text_locator.text
        # Make comparison to TRUE
        assert actual_text == "Logged In Successfully"

        # Verify button Log out is displayed on the new page
        logout_button_locator = driver.find_element(By.LINK_TEXT, "Log out")
        assert logout_button_locator.is_displayed()
