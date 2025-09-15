from selenium.webdriver.common.by import By

class SigneInPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to(self):
        self.driver.get("https://github.com/login")

    def try_login(self, username, password):
        login_elem = self.driver.find_element(By.ID, "login_field")
        login_elem.send_keys(username)

        password_elem = self.driver.find_element(By.ID, "password")
        password_elem.send_keys(password)

        sign_in_button = self.driver.find_element(By.NAME, "commit")
        sign_in_button.click()

        