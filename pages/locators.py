from selenium.webdriver.common.by import By

FIRST_NAME=(By.ID, "firstName")
LAST_NAME=(By.ID, "lastName")
USER_EMAIL=(By.ID, "userEmail")
GENDER=(By.CSS_SELECTOR, "label[for='gender-radio-{ID}']")
PHONE_NO=(By.ID, "userNumber")
DOB=(By.ID, "dateOfBirthInput")
DATE_MONTH=(By.CSS_SELECTOR, ".react-datepicker__month-select")
DATE_YEAR=(By.CSS_SELECTOR, ".react-datepicker__year-select")
DATE_DAY=(By.CSS_SELECTOR, ".react-datepicker__day--0{day}")
SUBJECT=(By.ID, "subjectsInput")
HOBBIES=(By.CSS_SELECTOR, "label[for='hobbies-checkbox-{ID}']")
PICTURE=(By.ID, "uploadPicture")
ADDRESS=(By.ID, "currentAddress")
STATE=(By.ID, "state")
CITY=(By.ID, "city")
SUBMIT=(By.ID, "submit")


