from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

# Set up Chrome options
options = Options()
options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Open the form URL
login_url = "https://demoqa.com/automation-practice-form"
driver.get(login_url)

# Fill in the form fields
driver.find_element(By.ID, "firstName").send_keys("Amisha")
driver.find_element(By.ID, "lastName").send_keys("Subedi")
driver.find_element(By.ID, "userEmail").send_keys("amishasubedi9@gmail.com")
driver.find_element(By.CSS_SELECTOR, "label[for='gender-radio-2']").click()
driver.find_element(By.ID, "userNumber").send_keys("6784567890")

# Enter date of birth
driver.find_element(By.ID, "dateOfBirthInput").click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, ".react-datepicker__month-select").send_keys("August")
driver.find_element(By.CSS_SELECTOR, ".react-datepicker__year-select").send_keys("2002")
driver.find_element(By.CSS_SELECTOR, ".react-datepicker__day--022").click()

# Enter subjects
subjects_input = driver.find_element(By.ID, "subjectsInput")
subjects_input.send_keys("Eng")
subjects_input.send_keys(Keys.RETURN)

# Select hobbies
driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-2']").click()
driver.find_element(By.CSS_SELECTOR, "label[for='hobbies-checkbox-3']").click()

# Upload picture
driver.find_element(By.ID, "uploadPicture").send_keys(r"c:\Users\gac\Desktop\as\shah-rukh-khan-indian-actor-bollywood-hd-wallpaper-preview.jpg")

# Enter current address
driver.find_element(By.ID, "currentAddress").send_keys("Devdaha, Rupandehi")

# Select state and city
state_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "state"))
)
driver.execute_script("arguments[0].scrollIntoView(true);", state_dropdown)

state_dropdown.click()
state_option = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'NCR')]"))
)
state_option.click()

city_dropdown = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.ID, "city"))
)
driver.execute_script("arguments[0].scrollIntoView(true);", city_dropdown)
city_dropdown.click()
city_option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Delhi')]"))
)
city_option.click()

# Submit the form

submit_button = WebDriverWait(driver, 10).until
EC.element_to_be_clickable((By.ID, "submit"))
driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

submit_button.click()


