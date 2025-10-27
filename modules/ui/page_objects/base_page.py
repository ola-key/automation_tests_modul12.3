import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self):
        options = Options()
        options.add_argument("start-maximized")
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36")
        # Не використовуємо headless, щоб уникнути блокування Amazon

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
    
    def wait_for_element(self, by, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, locator))
    )


    def close(self):
        self.driver.quit()