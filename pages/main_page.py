from pages.base import Base
from secret.login import LOGIN, PASSWORD

class MainPage(Base):
    def __init__(self, browser):
        super().__init__(browser)

    signin_button = '//button[@data-testid="header-default:button:open.sign-in-modal"]'
    email_input_field = '//input[@data-testid="auth-email"]'
    password_input_field = '//input[@data-testid="auth-password"]'
    login_button = '//button[@data-testid="sign-in-button"]'
    region_confirm_button = '//button[@data-testid="city-confirm:button:confirm"]'


    def authorize(self):
        '''Авторизация на сайте'''
        main_page_button = self.xpath_is_clicable(self.signin_button)
        main_page_button.click()

        email_field = self.xpath_is_visible(self.email_input_field)
        email_field.send_keys(LOGIN)

        password_field = self.xpath_is_visible(self.password_input_field)
        password_field.send_keys(PASSWORD)

        login_button = self.xpath_is_clicable(self.login_button)
        login_button.click()

    def confirm_region(self):
        '''Подтверждение региона (любого, который предлагает система'''
        button = self.xpath_is_clicable(self.region_confirm_button)
        button.click()
