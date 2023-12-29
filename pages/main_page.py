from pages.base import Base
from secret.login import LOGIN, PASSWORD

class MainPage(Base):
    def authorize(self, browser):
        main_page_button = self.xpath_locate_by(browser,
                                                '//button[@data-testid="header-default:button:open.sign-in-modal"]')
        main_page_button.click()
        email_field = self.xpath_locate_by(browser, '//input[@data-testid="auth-email"]')
        email_field.send_keys(LOGIN)
        password = self.xpath_locate_by(browser, '//input[@data-testid="auth-password"]')
        password.send_keys(PASSWORD)
        login_button = self.xpath_locate_by(browser, '//button[@data-testid="sign-in-button"]')
        login_button.click()

    def confirm_region(self, browser):
        button = self.xpath_locate_by(browser, '//button[@data-testid="city-confirm:button:confirm"]')
        button.click()