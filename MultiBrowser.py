from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from dotenv import load_dotenv
import os
load_dotenv()

# firefoxBinary = FirefoxBinary(os.getenv("FIREFOX_DRIVER"))
# driver = webdriver.Firefox(firefox_binary=firefoxBinary)
# driver = webdriver.Edge(executable_path=os.getenv("EDGE_DRIVER"))

driver = webdriver.Chrome(executable_path=os.getenv("CHROME_DRIVER"))
# driver = webdriver.Safari(executable_path=os.getenv("SAFARI_DRIVER"))

driver.get("https://www.nopcommerce.com/en/demo")
print(driver.title)

driver.close()
