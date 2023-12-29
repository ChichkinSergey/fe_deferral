import pytest
from pages.deferral_page import DeferralPage
from pages.main_page import MainPage
import time


@pytest.mark.deferral
class TestDeferralPage:
    @pytest.mark.smoke
    #https://qa-platferrum.testit.software/projects/2232/tests/17745
    #FE Оформление заявки - без документов
    def test_application_without_docs(self, browser):
        page = DeferralPage()
        page.open_page_and_authorize(browser)
        page.click_calculation_request_button(browser)
        page.click_next_first_screen(browser)
        time.sleep(5)