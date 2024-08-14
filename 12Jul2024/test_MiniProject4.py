# Selenium Project#4 - Mini Project
# open the url - https://katalon-demo-cura.herokuapp.com/ click on the make appointment button
# verify that url changes - assert time.sleep(3) enter the username, password next page verify the current url
# make appointment text on the web page.Upload them github.com

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure

def test_mini_project4():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # this get command opens the web page in the current session
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    btn_appointment = driver.find_element(By.ID, "btn-make-appointment")
    btn_appointment.click()

    # Verify if the URL changes

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(3)

    enter_user = driver.find_element(By.ID, "txt-username")
    enter_user.send_keys("John Doe")

    time.sleep(1)

    enter_user = driver.find_element(By.ID, "txt-password")
    enter_user.send_keys("ThisIsNotAPassword")

    time.sleep(1)

    btn_login = driver.find_element(By.ID, "btn-login")
    btn_login.click()

    time.sleep(3)

    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"

    text_appointment = driver.find_element(By.TAG_NAME, "h2")
    assert text_appointment.text == "Make Appointment"

    driver.quit()