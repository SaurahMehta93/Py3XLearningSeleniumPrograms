# 3- Selenium Mini Project Open the URL - https://www.idrive360.com/enterprise/login
# Enter the username, password Verify that Trial is finished and current URL also
# Add a logic to add Allure Screen for the Trail end

import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from allure_commons.types import AttachmentType


@allure.title("Selenium Mini Project")
@allure.description("Verify the login-webpage and find the error message")
@allure.tag("Web-Automation using selenium for idrive360 website")
@allure.severity("Medium")
@pytest.mark.Mini_Project
def test_mini_project3():
    driver = webdriver.Chrome()

    driver.get("https://www.idrive360.com/enterprise/login")
    time.sleep(5)
    driver.maximize_window()
    time.sleep(10)

    allure.attach(driver.get_screenshot_as_png(), name="webpage-screenshot", attachment_type=AttachmentType.PNG)

    user_name = driver.find_element(By.XPATH, "//input[@id='username']")
    user_name.send_keys("augtest_040823@idrive.com")
    time.sleep(5)

    pass_word = driver.find_element(By.XPATH, "//input[@id='password']")
    pass_word.send_keys("123456")
    time.sleep(5)

    # //button[ @ id = 'frm-btn']
    sign_in = driver.find_element(By.XPATH, "//button[@id ='frm-btn']")
    sign_in.click()
    time.sleep(10)

    allure.attach(driver.get_screenshot_as_png(), name="login-screenshot", attachment_type=AttachmentType.PNG)

    # //h5[@class='id-card-title']
    message_alert = driver.find_element(By.XPATH, "//h5[@class='id-card-title']")
    print(message_alert.text)
    time.sleep(5)
    assert message_alert.text == 'Your free trial has expired'
    allure.attach(driver.get_screenshot_as_png(), name="error_message-screenshot", attachment_type=AttachmentType.PNG)

    time.sleep(5)
    driver.quit()