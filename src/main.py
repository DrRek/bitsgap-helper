#!/usr/bin/python3
import os
import sys
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from decimal import Decimal

def to_decimal(num):
    '''
        Input: 
            '00001.10000'
        Output: Decimal('1.1')
        '''
    temp = Decimal(num)
    return temp.to_integral() if temp == temp.to_integral() else temp.normalize()

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

if "demo" in sys.argv:
    if "You are currently in Demo mode." not in driver.page_source:
        account_button = driver.find_element_by_css_selector("button.main-menu__button")
        account_button.click()
        switch_demo_button = driver.find_element_by_css_selector("div.switch__switch.switch__switch_color_green")
        switch_demo_button.click()
    if "You are currently in Demo mode." not in driver.page_source:
        print("Unable to verify if I'm on Demo mode")
        sys.exit(0)
    print("Using Demo Mode")
else:
    if "You are currently in Demo mode." in driver.page_source:
        account_button = driver.find_element_by_css_selector("button.main-menu__button")
        account_button.click()
        switch_demo_button = driver.find_element_by_css_selector("div.switch__switch.switch__switch_color_green")
        switch_demo_button.click()
    print("WARNING: Using Live Mode")

bots_rows = driver.find_elements_by_css_selector(".MuiTableRow-root.table__row.table__row_clickable")
for bot_row in bots_rows:
    bot_asset = bot_row.find_element_by_css_selector(".two-row-cell div").text
    bot_change_raw = bot_row.find_element_by_css_selector(".value-change__percents").text
    bot_change = to_decimal(bot_change_raw[:-1])
    print(bot_asset)
    print(bot_change)

driver.close()

