from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import os
load_dotenv()

driver = webdriver.Chrome(executable_path=os.getenv("CHROME_DRIVER"))

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")

# how to find how many input boxes in the page
input_boxes = driver.find_elements(By.CLASS_NAME, "text_field")
print(len(input_boxes))

# how to send keys to textbox
driver.find_element_by_id("RESULT_TextField-1").send_keys("Daaaaa")
driver.find_element_by_id("RESULT_TextField-2").send_keys("Reeeee")

driver.quit()
