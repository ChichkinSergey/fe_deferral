from pages.base import Base
from secret.login import LOGIN, PASSWORD

class MainPage(Base):
    def __init__(self, browser):
        super().__init__(browser)

    def authorize(self):
        main_page_button = self.xpath_is_clicable(
            '//button[@data-testid="header-default:button:open.sign-in-modal"]')
        main_page_button.click()

        email_field = self.xpath_is_visible('//input[@data-testid="auth-email"]')
        email_field.send_keys(LOGIN)

        password_field = self.xpath_is_visible('//input[@data-testid="auth-password"]')
        password_field.send_keys(PASSWORD)

        login_button = self.xpath_is_clicable('//button[@data-testid="sign-in-button"]')
        login_button.click()

    def confirm_region(self):
        button = self.xpath_is_clicable('//button[@data-testid="city-confirm:button:confirm"]')
        button.click()
