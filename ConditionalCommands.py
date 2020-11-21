from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time
load_dotenv()


driver = webdriver.Chrome(executable_path=os.getenv("CHROME_DRIVER"))
driver.get("http://demo.guru99.com/test/newtours/")

# get username textbox then send keys
userTxtBox = driver.find_element_by_name("userName")
userTxtBox.send_keys("mercury")

# get password textbox then send keys
passTxtBox = driver.find_element_by_name("password")
passTxtBox.send_keys("mercury")

# click the submit button
submintBtn = driver.find_element_by_name("submit").click()
loginTxt = driver.find_element_by_xpath(
    "//h3[contains(text(),'Login Successfully')]")

print(loginTxt.text == "Login Successfully")

# click the flight link
driver.find_element_by_xpath("//a[contains(text(),'Flights')]").click()

# get the radio button via css selector
round_ele = driver.find_element_by_css_selector("input[value=roundtrip]")

print(f'Radio Selected: {round_ele.is_selected()}')
driver.quit()
