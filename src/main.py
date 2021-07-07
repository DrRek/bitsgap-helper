import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

driver = webdriver.Chrome()
driver.get("https://app.bitsgap.com/bot")

login_email_field = driver.find_element_by_id("lemail")
if login_email_field:
    print("Trying to log in...")
    login_password_field = driver.find_element_by_id("lpassword")
    login_email_field.send_keys("hello")
    login_password_field.send_keys("test")

    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login-form button.btn-primary"))).click()

else:
    print("I'm already logged")

