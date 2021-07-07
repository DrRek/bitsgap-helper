#!/usr/bin/python3
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

#loading environments variables such as LOGIN_EMAIL and LOGIN_PASSWORD
load_dotenv()

options = Options()
options.add_argument("--user-data-dir=.selenium-browser-data")
options.add_argument('--profile-directory=profile')

driver = webdriver.Chrome(options=options)
driver.get("https://app.bitsgap.com/bot")

# Login
try:
    print("Trying to log in...")
    login_email_field = driver.find_element_by_id("lemail")
    login_password_field = driver.find_element_by_id("lpassword")
    login_email_field.send_keys(os.getenv("LOGIN_EMAIL"))
    login_password_field.send_keys(os.getenv("LOGIN_PASSWORD"))
    # I need to wait before login in because there is a loader that covers the click button
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login-form button.btn-primary"))).click()
    print("Login should be completed")
except NoSuchElementException:  #spelling error making this code not work as expected
    print("Users seems to be already logged")
    pass

