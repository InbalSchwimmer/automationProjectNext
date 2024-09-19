import allure
from allure_commons.types import Severity

from pages.home_category_page import HomeCategory


class TestHomeCategory:
    @allure.severity(Severity.CRITICAL)
    @allure.description("Verify click on home category will open homeware page by verifying the page url ")
    @allure.title("open homeware page from homepage")
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
        shopper.open_menu_category(shopper.HOME_CATEGORY_BTN)
        title = shopper.get_text(shopper.HOME_WARE_TITLE)
        assert title == "THE HOME SHOP"

    @allure.severity(Severity.NORMAL)
    @allure.description("Verify click on living room subcategory will open living room page by verifying the page url")
    @allure.title("open living room page from homeware")
    def test_open_living_room_subcategory(self):
        shopper = HomeCategory(self.driver)
        shopper.open_menu_category(shopper.HOME_CATEGORY_BTN)
        shopper.click(shopper.LIVING_ROOM_SUBCATEGORY)
        living_room_page_url = "https://www.next.co.il/en/shop/department-homeware-productaffiliation-livingroom-0"
        current_url = self.driver.current_url
        assert living_room_page_url == current_url

