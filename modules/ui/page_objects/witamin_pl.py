from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

class WitaminPage(BasePage):
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[type='search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    LOGO = (By.CSS_SELECTOR, "img[alt*='logo'], .logo")

    def open_homepage(self, url):
        self.driver.get(url)

    def search_for(self, term):
        self.enter_text(self.SEARCH_INPUT, term)
        self.click(self.SEARCH_BUTTON)

    def is_logo_visible(self):
        return self.is_visible(self.LOGO)

