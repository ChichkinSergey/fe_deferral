import pytest
from pages.deferral_page import DeferralPage


@pytest.mark.deferral
class TestDeferralPage:
    @pytest.mark.smoke
    #https://qa-platferrum.testit.software/projects/2232/tests/17745
    #FE Оформление заявки - без документов
    def test_application_without_docs(self, browser):
        page = DeferralPage(browser)
        page.open_page_and_authorize()
        page.click_calculation_request_button()
        page.click_next_1st_screen()
        page.click_5_million()
        page.click_next_2nd_screen()
        page.send_without_docs()
        assert page.check_modal_header(), "Не выводится правильный заголовок мод. окна"
        assert page.check_modal_text(), "Не выводится правильный текст в мод. окне"
        page.click_modal_exit_button()
        assert page.check_modal_is_invisible(), "Мод. окно не закрылось"
