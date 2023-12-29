from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Base:
    def xpath_locate_by(self, browser, xpath_locator):
        return WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_locator)))