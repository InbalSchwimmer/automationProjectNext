import allure
from allure_commons.types import Severity
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.home_category_page import HomeCategory
from pages.product_details_page import ProductDetails
from selenium.webdriver.support import expected_conditions as EC


class TestHomeCategory:
    @allure.severity(Severity.CRITICAL)
    @allure.description("Verify click on home category will open homeware page by verifying the page url ")
    @allure.title("Open homeware page from homepage")
    def test_open_homeware_page(self):
        shopper = HomeCategory(self.driver)
        shopper.open_menu_category(shopper.HOME_CATEGORY_BTN)
        home_category_url = "https://www.next.co.il/en/homeware"
        current_url = self.driver.current_url
        assert current_url == home_category_url

    @allure.severity(Severity.NORMAL)
    @allure.description("open subcategory 'homeware' and verify homeware title as design")
    @allure.title("Homeware page title")
    def test_homeware_title(self):
        shopper = HomeCategory(self.driver)
        with allure.step("Open homeware page - sub category 'Living room'"):
            shopper.open_menu_category(shopper.HOME_CATEGORY_BTN)
        with allure.step("Get homeware title and verify title is 'THE HOME SHOP'"):
            title = shopper.get_text(shopper.HOME_WARE_TITLE)
            assert title == "THE HOME SHOP"

    @allure.severity(Severity.NORMAL)
    @allure.description("Verify click on living room subcategory will open living room page by verifying the page url")
    @allure.title("Open living room page from homeware")
    def test_open_living_room_subcategory(self):
        shopper = HomeCategory(self.driver)
        with allure.step("Open homeware page - sub category 'Living room'"):
            shopper.open_living_room_subcategory()
        living_room_page_url = "https://www.next.co.il/en/shop/department-homeware-productaffiliation-livingroom-0"
        with allure.step("Verify url is"):
            current_url = self.driver.current_url
            assert living_room_page_url == current_url

    @allure.severity(Severity.NORMAL)
    @allure.description("Verify title of living room subcategory as design")
    @allure.title("Living room page title")
    def test_living_room_subcategory_title(self):
        shopper = HomeCategory(self.driver)
        with allure.step("Open homeware page - sub category 'Living room'"):
            shopper.open_living_room_subcategory()
        title = shopper.get_text(shopper.LIVING_ROOM_SUBCATEGORY_TITLE)
        with allure.step("Verify title of the page is 'All Living Room'"):
            assert title == "All Living Room"

    @allure.severity(Severity.NORMAL)
    @allure.description("Verify sort low to high price option will sort products as design")
    @allure.title("Sort page low to high")
    def test_sort_living_room_page_results_low_to_high(self):
        shopper = HomeCategory(self.driver)
        product = ProductDetails(self.driver)
        with allure.step("Open homeware page"):
            shopper.open_living_room_subcategory()
        with allure.step("Sort products results by price - low to high"):
            shopper.sort_page_results(shopper.SORT_BY_PRICE_LOW_HIGH)
            shopper.click(shopper.SORT_LOW_TO_HIGH_PRODUCT1)
        with allure.step("get price for two products"):
            price1 = shopper.get_price(product.PRODUCT_PRICE)
            shopper.driver.back()
            shopper.click(shopper.SORT_LOW_TO_HIGH_PRODUCT2)
            price2 = shopper.get_price(product.PRODUCT_PRICE)
        with allure.step("Verify first product price is less expensive than second product"):
            assert price1 < price2

    @allure.severity(Severity.NORMAL)
    @allure.description("Verify click on the product heart button will display red badge in top menu heart button")
    @allure.title("Active red badge - favorites")
    def test_favorite_product_active_badge(self):
        shopper = HomeCategory(self.driver)
        with allure.step("Open homeware page"):
            shopper.open_living_room_subcategory()
            shopper.sort_page_results(shopper.SORT_BY_PRICE_LOW_HIGH)
        with allure.step("Add product to favorites"):
            shopper.click(shopper.ADD_PRODUCT_TO_FAVORITES_BTN)
        with allure.step("Verify favorite bade display"):
            assert shopper.ACTIVE_FAVORITE_BADGE
        # take screenshot to verify favorites badge exist
        allure.attach(body=self.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.
                      attachment_type.PNG)
        shopper.click(shopper.REMOVE_PRODUCT_FROM_FAVORITES_BTN)

    @allure.severity(Severity.NORMAL)
    @allure.description("Verify remove product from favorites will remove favorites red badge from top menu")
    @allure.title("Inactive red badge - favorites")
    def test_favorite_product_inactive_badge(self):
        with allure.step("Open homeware page"):
            shopper = HomeCategory(self.driver)
            shopper.open_living_room_subcategory()
        with allure.step("Sort products results by price - low to high"):
            shopper.sort_page_results(shopper.SORT_BY_PRICE_LOW_HIGH)
        with allure.step("Add product to favorites"):
            shopper.click(shopper.ADD_PRODUCT_TO_FAVORITES_BTN)
        with allure.step("Remove product from favorites"):
            shopper.click(shopper.REMOVE_PRODUCT_FROM_FAVORITES_BTN)
        with allure.step("Verify favorite bade not display"):
            assert shopper.INACTIVE_FAVORITE_BADGE
        # take screenshot to verify favorites badge not exist
        allure.attach(body=self.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.
                      attachment_type.PNG)

    @allure.severity(Severity.NORMAL)
    @allure.description("Verify filter by colour will display product as was requested")
    @allure.title("Filter results by colour")
    def test_filter_products_list_by_colour(self):
        with allure.step("Open homeware page"):
            shopper = HomeCategory(self.driver)
            shopper.open_living_room_subcategory()
        with allure.step("Choose filter colour"):
            shopper.click(shopper.FILTER_BY_COLOR_BTN)
            shopper.click(shopper.BLUE_CHECK_BOX)
            shopper.sort_page_results(shopper.SORT_BY_PRICE_LOW_HIGH)
        with allure.step("Verify first product description contains 'Blue'"):
            first_blue_product = shopper.get_text(shopper.FIRST_HOMEWARE_BLUE_PRODUCT)
            assert "blue" in first_blue_product.lower()







