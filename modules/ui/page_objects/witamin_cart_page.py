from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from modules.ui.page_objects.base_page import BasePage
import time

class WitaminCartPage(BasePage):
    def __init__(self):
        super().__init__()

    def open_homepage(self):
        self.driver.get("https://witamin.pl")

    def click_produkty(self):
        wait = WebDriverWait(self.driver, 10)
        produkty = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="category-10"]/a')
        ))
        produkty.click()

    def click_first_product(self):
        wait = WebDriverWait(self.driver, 10)
        product = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="js-product-list"]/div/ul/li[1]/article/div[1]/div/a/img')
        ))
        product.click()

    def add_to_cart(self):
        wait = WebDriverWait(self.driver, 10)
        add_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[3]/div[1]/div[2]/div/button')
        ))
        add_button.click()

    def go_to_cart(self):
        wait = WebDriverWait(self.driver, 10)
        cart_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div[1]/a')
        ))
        cart_button.click()
        time.sleep(1)

    def proceed_to_checkout(self):
        wait = WebDriverWait(self.driver, 10)
        checkout_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div[2]/div/a')
        ))
        checkout_button.click()

