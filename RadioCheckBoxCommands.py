from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
import time
load_dotenv()

driver = webdriver.Chrome(executable_path=os.getenv("CHROME_DRIVER"))

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")


# check radio button if selected
radio = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(radio)

# select radio button
driver.find_element_by_xpath("//label[contains(text(),'Male')]").click()

# select status again
radio = driver.find_element_by_id("RESULT_RadioButton-7_0").is_selected()
print(radio)

# click checkbox
driver.find_element_by_xpath("//label[contains(text(),'Monday')]").click()
driver.find_element_by_xpath("//label[contains(text(),'Thursday')]").click()

# verify if selected
mon = driver.find_element_by_id(
    "RESULT_CheckBox-8_1").is_selected()
thur = driver.find_element_by_id(
    "RESULT_CheckBox-8_4").is_selected()

time.sleep(3)

print(mon)
print(thur)

driver.quit()
