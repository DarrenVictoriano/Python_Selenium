from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from dotenv import load_dotenv
import os
import time
load_dotenv()


driver = webdriver.Chrome(executable_path=os.getenv("CHROME_DRIVER"))
driver.get("https://www.expedia.com/")

# implicit wait
driver.implicitly_wait(10)

# click flight btn
driver.find_element_by_xpath(
    "//a[contains(@href,'?pwaLob=wizard-flight-pwa')]").click()
time.sleep(2)

# Enter SAN to departing location
driver.find_element_by_xpath(
    "//button[contains(@aria-label, 'Leaving from')]").click()

driver.find_element_by_id("location-field-leg1-origin").send_keys("SAN")

driver.find_element_by_id("location-field-leg1-origin").send_keys(Keys.ENTER)

# Enter NYC to arrival location
driver.find_element_by_xpath(
    "//button[contains(@aria-label, 'Going to')]").click()

driver.find_element_by_id("location-field-leg1-destination").send_keys("NYC")

driver.find_element_by_id(
    "location-field-leg1-destination").send_keys(Keys.ENTER)
time.sleep(1)

# Select date
driver.find_element_by_id("d1-btn").click()
time.sleep(1)
driver.find_element_by_xpath(
    "//button[contains(@aria-label, 'Nov 28')]").click()
time.sleep(1)
driver.find_element_by_xpath(
    "//button[contains(@aria-label, 'Dec 1')]").click()
time.sleep(1)
driver.find_element_by_xpath(
    "//button[contains(@data-stid, 'apply-date-picker')]").click()
time.sleep(1)

# click search
driver.find_element_by_xpath("//button[contains(text(),'Search')]").click()

# explicit wait until radio_nonstop is clickable
wait = WebDriverWait(driver, 10)
radio_nonstop = wait.until(lambda driver: driver.find_element_by_id("stops-0"))
# radio_nonstop = wait.until(EC.element_to_be_clickable((By.ID, "stops-0")))

# then click it
radio_nonstop.click()

time.sleep(5)
driver.quit()
