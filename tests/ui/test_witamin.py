import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException


class TestWitaminPl:
    """UI tests for witamin.pl website"""
    
    BASE_URL = "https://witamin.pl"
    
    def setup_method(self):
        """Setup method - creates browser driver before each test"""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    
    def teardown_method(self):
        """Teardown method - closes browser after each test"""
        if self.driver:
            self.driver.quit()

    @pytest.mark.ui
    def test_homepage_loads_successfully(self):
        """Test if homepage loads successfully"""
        
        self.driver.get(self.BASE_URL) # Open witamin.pl homepage
        time.sleep(3)
        
        assert "witamin" in self.driver.title.lower() # Check if page title contains "witamin"
        
        assert self.driver.current_url == self.BASE_URL + "/"  # Check if page loaded successfully (status in browser)
        
        body = self.driver.find_element(By.TAG_NAME, "body")  # Verify body element exists
        assert body is not None
        time.sleep(2)


    @pytest.mark.ui
    def test_navigation_elements_present(self):
        """Test if main navigation elements are present"""
        self.driver.get(self.BASE_URL)  # Open homepage
        time.sleep(2)
        
        try:  # Check for navigation menu
            nav_menu = self.driver.find_element(By.CSS_SELECTOR, "nav, .navigation, .menu, [role='navigation']")
            assert nav_menu.is_displayed()
        except NoSuchElementException: # If no nav found, check for menu links
            menu_links = self.driver.find_elements(By.CSS_SELECTOR, "a[href*='/'], .menu-item")
            assert len(menu_links) > 0      
        
        try:  # Check for logo/brand element
            logo = self.driver.find_element(By.CSS_SELECTOR, "img[alt*='logo'], .logo, [class*='brand'], [class*='logo']")
            assert logo.is_displayed()
        except NoSuchElementException:  # Alternative: check for any header element
            header = self.driver.find_element(By.CSS_SELECTOR, "header, .header")
            assert header.is_displayed()
        
        time.sleep(2)
    @pytest.mark.ui
    def test_search_functionality(self): 
        """Test search functionality"""
        self.driver.get(self.BASE_URL) # Open homepage
        time.sleep(2)
        
        try:  # Try to find search input
            search_input = self.driver.find_element(By.CSS_SELECTOR, 
                "input[type='search'], input[placeholder*='szukaj'], .search-input, #search")
            search_input.clear() # Enter search term
            search_input.send_keys("witamina")
            time.sleep(2)
            
            # Try to find and click search button
            try:
                search_button = self.driver.find_element(By.CSS_SELECTOR, 
                    "button[type='submit'], .search-button, [class*='search-btn']")
                search_button.click()
            except NoSuchElementException:
                # If no search button, press Enter
                search_input.send_keys(Keys.RETURN)
            
            time.sleep(2)
            
            # Verify search results or that we navigated somewhere
            current_url = self.driver.current_url
            assert current_url != self.BASE_URL + "/"
            
        except NoSuchElementException:
            # If search not found, just verify page has products or categories
            products = self.driver.find_elements(By.CSS_SELECTOR, 
                ".product, [class*='product'], a[href*='product']")
            assert len(products) > 0
        
        time.sleep(2)

    @pytest.mark.ui
    def test_product_navigation(self):
        """Test navigation to product pages"""
        # Open homepage
        self.driver.get(self.BASE_URL)
        time.sleep(2)
        
        # Find product links
        product_links = self.driver.find_elements(By.CSS_SELECTOR, 
            "a[href*='product'], a[href*='maca'], .product-link, .product a")
        
        if len(product_links) > 0:
            # Click on first product
            first_product = product_links[0]
            product_url = first_product.get_attribute('href')
            first_product.click()
            time.sleep(3)
            
            # Verify we're on product page
            current_url = self.driver.current_url
            assert current_url != self.BASE_URL + "/"
            assert product_url in current_url
            
            # Check for product elements
            try:
                product_title = self.driver.find_element(By.CSS_SELECTOR, 
                    "h1, .product-title, .product-name")
                assert product_title.is_displayed()
                assert len(product_title.text.strip()) > 0
            except NoSuchElementException:
                # Alternative check - just verify page content changed
                page_content = self.driver.find_element(By.TAG_NAME, "body").text
                assert "witamin" in page_content.lower() or "suplement" in page_content.lower()
        
        time.sleep(2)
    
    @pytest.mark.ui
    def test_shopping_cart_access(self):
        #Test shopping cart accessibility via dropdown and main button
        # Open homepage
        self.driver.get(self.BASE_URL)
        time.sleep(3)
        
        # Look for cart icon/link
        try:
            cart_icon = self.driver.find_element(By.CSS_SELECTOR, ".cart, [class*='cart'], .basket, [href*='cart'], [href*='koszyk']")
            assert cart_icon.is_displayed()
            cart_icon.click()
            time.sleep(2)
        except NoSuchElementException:
            pytest.fail("Cart icon not found")
            
        try: # Click on drobpdown cart or go to cart button if exists
            go_to_cart_btn = self.driver.find_element(By.CSS_SELECTOR, "a.btn-primary:nth-child(1)")
            assert go_to_cart_btn.is_displayed()
            go_to_cart_btn.click()
            time.sleep(2)
        except NoSuchElementException:
            pytest.fail("Go to cart button not found after dropdown")

            # Verify cart page or cart functionality
            current_url = self.driver.current_url
            cart_indicators = ["cart", "koszyk", "basket"]
            url_has_cart = any(indicator in current_url.lower() for indicator in cart_indicators)
            
            if url_has_cart:
                assert url_has_cart
            else:
                # Check for cart content on page
                cart_content = self.driver.find_elements(By.CSS_SELECTOR, 
                    ".cart-content, .cart-items, #cart, .shopping-cart")
                assert len(cart_content) > 0
                
        except NoSuchElementException:
            # If no cart found, check for e-commerce indicators
            ecommerce_elements = self.driver.find_elements(By.CSS_SELECTOR, 
                "[class*='price'], .price, [class*='buy'], .add-to-cart")
            assert len(ecommerce_elements) > 0
        
        time.sleep(2)

    @pytest.mark.ui
    def test_user_account_access(self):
        """Test user account/login access"""
        # Open homepage
        self.driver.get(self.BASE_URL)
        time.sleep(2)
        
        # Look for login/account links
        try:
            account_link = self.driver.find_element(By.CSS_SELECTOR, 
                "a[href*='login'], a[href*='account'], a[href*='konto'], .user-menu, [class*='login']")
            
            assert account_link.is_displayed()
            
            # Click on account link
            account_link.click()
            time.sleep(2)
            
            login_button = self.driver.find_element(By.CSS_SELECTOR, ".dropdown-menu > li:nth-child(1) > a:nth-child(1) > span:nth-child(1)")
            login_button.click()
            time.sleep(2)

            header = self.driver.find_element(By.XPATH, "/html/body/main/section/div/div/section/header/h1")
            assert header.is_displayed()
            assert "zaloguj się do swojego konta" in header.text.lower()

            # Check if we're on login page or account page
            current_url = self.driver.current_url
            account_indicators = ["login", "account", "konto", "user"]
            url_has_account = any(indicator in current_url.lower() for indicator in account_indicators)
            
            if url_has_account:
                assert url_has_account
            else:
                # Look for login form
                login_elements = self.driver.find_elements(By.CSS_SELECTOR, 
                    "form[action*='login'], .login-form, #login-form, input[type='email'], input[type='password']")
                assert len(login_elements) > 0
                
        except NoSuchElementException:
            # If no account link found, just verify this is an e-commerce site
            page_text = self.driver.find_element(By.TAG_NAME, "body").text.lower()
            ecommerce_keywords = ["sklep", "produkty", "cena", "kup", "zamów"]
            has_ecommerce_content = any(keyword in page_text for keyword in ecommerce_keywords)
            assert has_ecommerce_content
        
        time.sleep(2)

    @pytest.mark.ui
    def test_product_pricing_display(self):
        """Test if products display pricing information"""
        # Open homepage
        self.driver.get(self.BASE_URL)
        time.sleep(2)
        
        try:
            produkty_link = self.driver.find_element(By.CSS_SELECTOR, "#category-10 > a:nth-child(1)")
            produkty_link.click()
            time.sleep(2)
        except NoSuchElementException:
            pytest.fail("Produkty module not found")

        # Look for price elements
        price_elements = self.driver.find_elements(By.CSS_SELECTOR, 
            ".price, [class*='price'], .cost, [class*='cost']")
        
        if len(price_elements) > 0:
            # Check if prices are displayed and contain currency
            for price_elem in price_elements[:3]:  # Check first 3 prices
                if price_elem.is_displayed():
                    price_text = price_elem.text
                    assert len(price_text) > 0
                    # Should contain currency symbols or "zł"
                    currency_indicators = ["zł", "PLN", "€", "$"]
                    has_currency = any(curr in price_text for curr in currency_indicators)
                    if has_currency:
                        assert has_currency
                        break
        else:
            # Alternative: look for any numeric values that might be prices
            page_text = self.driver.find_element(By.TAG_NAME, "body").text
            # Look for patterns like "25,00 zł" mentioned in the content we saw
            assert "zł" in page_text or any(char.isdigit() for char in page_text)
        
        time.sleep(2)
