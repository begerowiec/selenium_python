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
        'phone_number': ('ID', 'inputPhone'),
        'company_name': ('ID', 'inputCompanyName'),
        'street_address': ('ID', 'inputAddress1'),
        'city': ('ID', 'inputCity'),
        'country': ('ID', 'inputCountry'),
        'poland_country': ('XPATH', '//*[@id="inputCountry"]/option[177]')

    }

    def enter_personal_information(self):
        self.first_name.set_text('Selenium')
        self.last_name.set_text('WebDriver')
        self.email.set_text('test@wbd.adi')
        self.dial_code.click()
        self.polish_dial_code.click()
        self.phone_number.set_text('070032154')

    def enter_billing_address(self):
        self.company_name.set_text('Testers Company')
        self.street_address.set_text('AutoTestStreet 2/5')
        self.city.set_text('Gotham')
        self.country.click()
        self.poland_country.click()
