from pages.base import Base
from pages.main_page import MainPage
class DeferralPage(Base):
    def open_defferal_page(self, browser):
        browser.get('https://mf-shell-app-staging.metalplatform.ru/services/otsrochka')

    def open_page_and_authorize(self, browser):
        main_page = MainPage()
        self.open_defferal_page(browser)
        main_page.confirm_region(browser)
        main_page.authorize(browser)

    def scroll_to_buttons(self, browser):
        buttons = self.xpath_locate_by(browser, '//button[.//span[contains(text(), "Запросить расчет")]]')
        browser.execute_script("arguments[0].scrollIntoView();", buttons)

    def click_calculation_request_button(self, browser):
        self.scroll_to_buttons(browser)
        button = self.xpath_locate_by(browser, '//button[.//span[contains(text(), "Запросить расчет")]]')
        button.click()

    def click_next_first_screen(self, browser):
        button = self.xpath_locate_by(browser, '//button[@data-testid="deferral-request-form-info:button:submit"]')
        button.click()



