from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Base:
    def __init__(self, browser):
        self.browser = browser
    def xpath_is_clicable(self, xpath_locator: str):
        return WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_locator)))

    def xpath_is_visible(self, xpath_locator: str):
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.XPATH, xpath_locator)))

    def xpath_is_not_visible(self, xpath_locator: str):
        return WebDriverWait(self.browser, 10).until(
            EC.invisibility_of_element_located((By.XPATH, xpath_locator)))