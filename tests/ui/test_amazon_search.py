import pytest
from modules.ui.page_objects.amazon_search_page import AmazonSearchPage

@pytest.mark.ui
def test_amazon_sort_by_best_sellers():
    page = AmazonSearchPage()

    page.go_to_homepage()
    page.search_product("wireless headphones")
    page.apply_sorting_best_sellers()
    page.close()
    