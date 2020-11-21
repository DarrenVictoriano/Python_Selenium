from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
from dotenv import load_dotenv
load_dotenv()

driver = webdriver.Chrome(executable_path=os.getenv("CHROME_DRIVER"))

# navigate to specified URL
driver.get("http://demo.guru99.com/test/newtours/")
time.sleep(5)
print(driver.title)

# navigate to specified URL
driver.get("https://www.pavantestingtools.com")
time.sleep(5)
print(driver.title)

# press browser's back button
driver.back()
time.sleep(5)
print(driver.title)

# press browser's forward button
driver.forward()
time.sleep(5)
print(driver.title)
