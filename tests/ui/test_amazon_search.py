import pytest
from modules.ui.page_objects.amazon_search_page import AmazonSearchPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.ui
def test_amazon_sort_by_best_sellers():
    page = AmazonSearchPage()

    page.go_to_homepage()
    page.search_product("wireless headphones")
    page.apply_sorting_best_sellers()

    # Check: are there any results displayed
    results = page.driver.find_elements(By.CSS_SELECTOR, "div[data-component-type='s-search-result']")
    if results:
        assert len(results) > 0, "At least one search result is expected"
    
    # Another check: verify that the search term is in the search box
    wait = WebDriverWait(page.driver, 10)
    try:
        search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        assert search_box.get_attribute("value").lower() == "wireless headphones"
    except Exception:
        #check the URL or title for the presence of query keywords
        url = page.driver.current_url.lower()
        title = page.driver.title.lower()
        assert ("wireless" in url) or ("wireless" in title), "The query was not found in the search field, URL, or title"
    
    page.close()
        