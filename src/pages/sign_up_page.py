from seleniumpagefactory.Pagefactory import PageFactory

class SignUpPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'first_name': ('ID', 'inputFirstName'),
        'last_name': ('ID', 'inputLastName'),
        'email': ('ID', 'inputEmail'),
        'dial_code': ('XPATH', '//*[@id="containerNewUserSignup"]/div[1]/div/div/div[4]/div/div/div/div/div[2]'),
        'polish_dial_code': ('XPATH', '//*[@id="containerNewUserSignup"]/div[1]/div/div/div[4]/div/div/div/ul/li['
                                      '175]/span[1]'),
        'phone_number': ('ID', 'inputPhone')
    }

    def enter_first_name(self):
        self.first_name.set_text('Selenium')

    def enter_last_name(self):
        self.last_name.set_text('WebDriver')

    def enter_email(self):
        self.email.set_text('test@wbd.adi')

    def enter_phone(self):
        self.dial_code.click()
        self.polish_dial_code.click()
        self.phone_number.set_text('070032154')
