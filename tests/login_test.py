import time
from pages.login import LoginPage
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get('https://demoqa.com/automation-practice-form') 
    yield driver
    driver.quit()

def test_login(driver):
    login_page = LoginPage(driver)
    login_page.enter_firstname('Amisha')
    login_page.enter_lastname('Subedi')
    login_page.enter_email('abc@gmail.com')
    login_page.enter_address('ghd')
    login_page.enter_gender("F")
    login_page.enter_ph_no('7898786544')
    login_page.enter_pic(r"c:\Users\gac\Desktop\as\shah-rukh-khan-indian-actor-bollywood-hd-wallpaper-preview.jpg")
    login_page.enter_DOB(20,"August","2002")
    login_page.enter_subject("English")
    login_page.enter_hobbies(["1","2"])
    login_page.enter_state_city("NCR","Delhi")
    login_page.submit()
    time.sleep(20)