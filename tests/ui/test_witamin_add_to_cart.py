import pytest
from modules.ui.page_objects.witamin_cart_page import WitaminCartPage

@pytest.mark.ui
def test_add_item_to_cart_witamin():
    page = WitaminCartPage()

    page.open_homepage()
    page.click_produkty()
    page.click_first_product()
    page.add_to_cart()
    page.go_to_cart()
    page.proceed_to_checkout()
    page.close()
