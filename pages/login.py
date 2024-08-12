from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import FIRST_NAME,LAST_NAME, SUBMIT,USER_EMAIL,DATE_MONTH,DATE_DAY,DATE_YEAR,DOB,GENDER,PHONE_NO,PICTURE,HOBBIES,SUBJECT,ADDRESS,STATE,CITY
from selenium.webdriver.common.keys import Keys


class LoginPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.first_name_field = FIRST_NAME
        self.last_name_field = LAST_NAME
        self.email = USER_EMAIL
        self.DOB = DOB 
        self.DOM = DATE_MONTH
        self.DOY = DATE_YEAR
        self.DOD = DATE_DAY
        self.gender = GENDER
        self.ph_no = PHONE_NO
        self.hobbies = HOBBIES
        self.pic = PICTURE
        self.address = ADDRESS
        self.subject = SUBJECT
        self.state = STATE
        self.city = CITY
        self.submit_button = SUBMIT




    def enter_firstname(self, firstname: str):
        self.driver.find_element(*self.first_name_field).send_keys(firstname)

    def enter_lastname(self, lastname: str):
        self.driver.find_element(*self.last_name_field).send_keys(lastname)

    
    def enter_email(self, email: str):
        self.driver.find_element(*self.email).send_keys(email)

    def enter_DOB(self, day:int,month:str,year:str):
        self.driver.find_element(*self.DOB).click()
        self.driver.find_element(*self.DOY).send_keys(year)
        self.driver.find_element(*self.DOM).send_keys(month)
        day = (self.DOD[0],self.DOD[1].format(day=str(day)))
        self.driver.find_element(*day).click()



    def enter_subject(self, subject: str):
        self.driver.find_element(*self.subject).send_keys(subject)
        self.driver.find_element(*self.subject).send_keys(Keys.RETURN)


    def enter_address(self, address: str):
        self.driver.find_element(*self.address).send_keys(address)

    def enter_pic(self, pic: str):
        self.driver.find_element(*self.pic).send_keys(pic)

    def enter_hobbies(self, hobbies: list):
        for each_hobby in hobbies:
            selected_hobbies = (self.hobbies[0],self.hobbies[1].format(ID=each_hobby))
            self.driver.find_element(*selected_hobbies).click()


    def enter_ph_no(self, ph_no: str):
        self.driver.find_element(*self.ph_no).send_keys(ph_no)

    def enter_gender(self, gender):
        if gender == "F":
            selected_gender = (self.gender[0],self.gender[1].format(ID=2))
        else:
            selected_gender = (self.gender[0],self.gender[1].format(ID=1))

        self.driver.find_element(*selected_gender).click()

    def enter_state_city(self, state,city):

        state_dropdown = WebDriverWait(self.driver, 10).until(
    EC.element_to_be_clickable(self.state)
)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", state_dropdown)

        state_dropdown.click()
        state_option = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(),'{state}')]"))
        )
        state_option.click()

        city_dropdown = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.city)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", city_dropdown)
        city_dropdown.click()
        city_option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[contains(text(),'{city}')]"))
        )
        city_option.click()


    def submit(self):
        self.driver.find_element(*self.submit_button).click()

        # submit_button = WebDriverWait(self.driver, 10).until
        # EC.element_to_be_clickable(self.submit_button)
        # self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)

        #submit_button.click()




            
