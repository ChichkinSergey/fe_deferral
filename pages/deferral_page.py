from pages.base import Base
from pages.main_page import MainPage

class DeferralPage(Base):
    def __init__(self, browser):
        super().__init__(browser)

        # Локаторы страницы отсрочки
        self.link = 'https://mf-shell-app-staging.metalplatform.ru/services/otsrochka'
        self.left_button = '//div[text()="Базовый"]//following-sibling::button'
        self.central_button = '//div[text()="Расширенный"]//following-sibling::button'
        self.right_button = '//div[text()="Максимальный"]//following-sibling::button'

        # Локаторы первого экрана
        self.next_1st_screen = '//button[@data-testid="deferral-request-form-info:button:submit"]'
        self.cancel_1st_screen = '//button[.//span[text()="Отменить"]]'
        # Вот тут нужна помощь. Не работает:
        # //div[normalize-space()='Заявка на подключение отсрочки от Платферрум']
        self.header_1st_screen = '//div[contains(text(), "Заявка на") and contains(text(), "подключение отсрочки от") and contains(text(), "Платферрум")]'

        # Локаторы второго экрана
        self.five_million = '//div[@role="button"][.//span[text()="до 5 млн ₽"]]'
        self.next_2nd_screen = '//button[@data-testid="deferral-request-limit:button:submit"]'

        # Локаторы третьего экрана
        self.submit_without_docs = '//button[@data-testid="deferral-request-files:button:without-files"]'

        # Локаторы модального окна после подачи заявки
        self.modal_header = '//header//div[text()="Заявка успешно отправлена"]'
        self.modal_exit = '//button[.//span[text() = "Вернуться на сайт"]]'
        # Вот тут нужна помощь. Не работает:
        # //div[contains(normalize-space(), "Наши специалисты свяжутся с вами в ближайшее время.")]
        self.modal_text = '//div[contains(text(), "Наши специалисты свяжутся с") and contains(text(), "вами в") and contains(text(), "ближайшее время.")]'

    def open_deferral_page(self):
        self.browser.get(self.link)

    def open_page_and_authorize(self):
        main_page = MainPage(self.browser)
        self.open_deferral_page()
        main_page.confirm_region()
        main_page.authorize()

    def scroll_to_left_button(self):
        button = self.xpath_is_clicable(self.left_button)
        self.browser.execute_script("arguments[0].scrollIntoView();", button)

    def scroll_to_right_button(self):
        button = self.xpath_is_clicable(self.right_button)
        self.browser.execute_script("arguments[0].scrollIntoView();", button)

    def click_left_calc_request_button(self):
        self.scroll_to_left_button()
        button = self.xpath_is_clicable(self.left_button)
        button.click()

    def click_central_calc_request_button(self):
        button = self.xpath_is_clicable(self.central_button)
        button.click()

    def click_right_calc_request_button(self):
        self.scroll_to_right_button()
        button = self.xpath_is_clicable(self.right_button)
        button.click()

    def click_next_1st_screen(self):
        button = self.xpath_is_clicable(self.next_1st_screen)
        button.click()

    def click_cancel_1st_screen(self):
        button = self.xpath_is_clicable(self.cancel_1st_screen)
        button.click()

    def click_5_million(self):
        button = self.xpath_is_clicable(self.five_million)
        button.click()

    def click_next_2nd_screen(self):
        button = self.xpath_is_clicable(self.next_2nd_screen)
        button.click()

    def send_without_docs(self):
        button = self.xpath_is_clicable(self.submit_without_docs)
        button.click()

    def check_success_submission_header(self):
        self.xpath_is_visible(self.modal_header)
        return True

    def check_1st_screen_header(self):
        header = self.xpath_is_visible(self.header_1st_screen)
        assert header.text == 'Заявка на подключение отсрочки от Платферрум', "Не выводится правильный заголовок мод. окна"

    def check_success_submission_text(self):
        self.xpath_is_visible(self.modal_text)
        return True

    def click_success_submission_exit_button(self):
        button = self.xpath_is_clicable(self.modal_exit)
        button.click()

    def check_success_submission_is_invisible(self):
        self.xpath_is_not_visible(self.modal_header)
        return True
