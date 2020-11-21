from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
import time
load_dotenv()

# Chrome
driver = webdriver.Chrome(executable_path=os.getenv("CHROME_DRIVER"))

# open URL
driver.get("http://demo.automationtesting.in/Register.html")

firstNameInput = driver.find_element_by_xpath(
    "//body/section[@id='section']/div[1]/div[1]/div[2]/form[1]/div[1]/div[1]/input[1]")
firstNameInput.send_keys("What's up?")

time.sleep(5)
driver.quit()
