import pytest
from modules.ui.page_objects.amazon_search_page import AmazonSearchPage
from selenium.webdriver.common.by import By

@pytest.mark.ui
def test_amazon_sort_by_best_sellers():
    page = AmazonSearchPage()

    page.go_to_homepage()
    page.search_product("wireless headphones")
    page.apply_sorting_best_sellers()

    # Перевірка: чи є результати
    results = page.driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")

    assert len(results) > 0, "Очікується хоча один результат пошуку"
    
    page.close()
        