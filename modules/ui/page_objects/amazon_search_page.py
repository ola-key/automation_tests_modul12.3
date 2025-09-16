from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from modules.ui.page_objects.base_page import BasePage

class AmazonSearchPage(BasePage):
    def __init__(self):
        super().__init__()

    def go_to_homepage(self):
        self.driver.get("https://www.amazon.com")
        self.bypass_bot_protection()

    def bypass_bot_protection(self):
        try:
            wait = WebDriverWait(self.driver, 5)
            continue_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Continue shopping')]")
            ))
            continue_button.click()
        except:
            pass  # Якщо захист не з’явився — просто ігноруємо

    def search_product(self, query):
        wait = WebDriverWait(self.driver, 10)
        search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

    def apply_sorting_best_sellers(self):
        wait = WebDriverWait(self.driver, 10)

        # Клік по дропдауну сортування
        sort_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "a-autoid-0-announce")))
        sort_dropdown.click()

        # Вибір пункту "Best Sellers"
        best_sellers_option = wait.until(EC.element_to_be_clickable((By.ID, "s-result-sort-select_5")))
        best_sellers_option.click()
