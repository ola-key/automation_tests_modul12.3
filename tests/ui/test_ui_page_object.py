import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from modules.ui.page_objects.sign_in_page import SigneInPage

@pytest.mark.ui
def test_check_incorrect_username_page_object():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    sign_in_page = SigneInPage(driver)
    sign_in_page.go_to()
    sign_in_page.try_login("page_object@gmail.com", "wrong password")

    # Перевірка повідомлення про помилку
    assert "Incorrect username or password." in driver.page_source

    driver.quit()
    