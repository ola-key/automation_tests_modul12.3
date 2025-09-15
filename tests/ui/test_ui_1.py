import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


@pytest.mark.ui
def test_check_incorrect_username():
    #створення об.єкту для керування браузером
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    #відкриваємо сторінку http://github.com/login
    driver.get("http://github.com/login")

    #Знаходимо поле, в яке будемо вводити неправильне ім.я користувача
    login_elem = driver.find_element(By.ID, "login_field")
    
    #вводимо неправильне ім.я користувача або електронну адресу
    login_elem.send_keys("lifeproject42@igmail.com")
    time.sleep(3)

    #знаходимо поле, в яке будемо вводити неправильний пароль
    pass_elem = driver.find_element(By.ID, "password")

    #вводимо неправильний пароль
    pass_elem.send_keys("wrong password")
    time.sleep(3)

    #знаходимо кнопку signe in
    btn_elem = driver.find_element(By.NAME, "commit")

    #клікаємо на кнопку
    btn_elem.click()
    time.sleep(3)
    

    # перевіряємо що назва сторінки така, яку ми очікуємо
    assert driver.title == "Sign in to GitHub · GitHub"
    time.sleep(3)

    driver.close() 

    