from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from modules.ui.page_objects.base_page import BasePage

class WitaminCartPage(BasePage):
    def __init__(self, timeout: int = 10):
        super().__init__()
        self.timeout = timeout

    def open_homepage(self):
        self.driver.get("https://witamin.pl")
        return self

    def click_produkty(self):
        try:
            produkty = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="category-10"]/a'))
            )
            produkty.click()
        except TimeoutException:
            raise TimeoutException("Category 'produkty' not clickable or not found")
        return self

    def click_first_product(self):
        try:
            product = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="js-product-list"]/div/ul/li[1]/article/div[1]/div/a/img'))
            )
            product.click()
        except TimeoutException:
            raise TimeoutException("First product not clickable or not found")
        return self

    def add_to_cart(self):
        try:
            add_button = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[3]/div[1]/div[2]/div/button'))
            )
            add_button.click()
        except TimeoutException:
            raise TimeoutException("Add to cart button not clickable or not found")
        return self

    def go_to_cart(self):
        try:
            cart_button = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div[1]/a'))
            )
            cart_button.click()
            # wait for cart page/modal to appear instead of sleep
            WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.cart-container, #blockcart-modal"))
            )
        except TimeoutException:
            raise TimeoutException("Cart button/modal did not appear")
        return self

    def proceed_to_checkout(self):
        try:
            checkout_button = WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div[2]/div/a'))
            )
            checkout_button.click()
        except TimeoutException:
            raise TimeoutException("Checkout button not clickable or not found")
        return self

