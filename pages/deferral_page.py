from pages.base import Base
from pages.main_page import MainPage

class DeferralPage(Base):
    def __init__(self, browser):
        super().__init__(browser)

    def open_deferral_page(self):
        self.browser.get('https://mf-shell-app-staging.metalplatform.ru/services/otsrochka')

    def open_page_and_authorize(self):
        main_page = MainPage(self.browser)
        self.open_deferral_page()
        main_page.confirm_region()
        main_page.authorize()

    def scroll_to_buttons(self):
        buttons = self.xpath_is_clicable('//button[.//span[contains(text(), "Запросить расчет")]]')
        self.browser.execute_script("arguments[0].scrollIntoView();", buttons)

    def click_calculation_request_button(self):
        self.scroll_to_buttons()
        button = self.xpath_is_clicable('//button[.//span[contains(text(), "Запросить расчет")]]')
        button.click()

    def click_next_1st_screen(self):
        button = self.xpath_is_clicable('//button[@data-testid="deferral-request-form-info:button:submit"]')
        button.click()

    def click_5_million(self):
        button = self.xpath_is_clicable('//div[@role="button"][.//span[text()="до 5 млн ₽"]]')
        button.click()

    def click_next_2nd_screen(self):
        button = self.xpath_is_clicable('//button[@data-testid="deferral-request-limit:button:submit"]')
        button.click()

    def send_without_docs(self):
        button = self.xpath_is_clicable('//button[@data-testid="deferral-request-files:button:without-files"]')
        button.click()

    def check_modal_header(self):
        self.xpath_is_visible('//header//div[text()="Заявка успешно отправлена"]')
        return True

    def check_modal_text(self):
        # Вот тут нужна помощь. Не работает:
        # //div[contains(normalize-space(), "Наши специалисты свяжутся с вами в ближайшее время.")]
        # Пришлось изголяться
        self.xpath_is_visible('//div[contains(text(), "Наши специалисты свяжутся с") and contains(text(), "вами в") and contains(text(), "ближайшее время.")]')
        return True

    def click_modal_exit_button(self):
        button = self.xpath_is_clicable('//button[.//span[text() = "Вернуться на сайт"]]')
        button.click()

    def check_modal_is_invisible(self):
        self.xpath_is_not_visible('//header//div[text()="Заявка успешно отправлена"]')
        return True
