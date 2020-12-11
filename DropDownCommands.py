from selenium import webdriver
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv
import os
load_dotenv()

driver = webdriver.Chrome(executable_path=os.getenv("CHROME_DRIVER"))
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

drp = Select(driver.find_element_by_id("RESULT_RadioButton-9"))
drp.select_by_visible_text("Afternoon")

driver.quit()
