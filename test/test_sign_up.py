import time

from selenium import webdriver
from src.pages.sign_up_page import SignUpPage

def test_SignUp():
    driver = webdriver.Chrome(executable_path='C:\\bin\\chromedriver.exe')
    driver.get('https://phptravels.org/register.php')

    sign_up_page = SignUpPage(driver)

    sign_up_page.enter_personal_information()
    sign_up_page.enter_billing_address()
    time.sleep(5)
