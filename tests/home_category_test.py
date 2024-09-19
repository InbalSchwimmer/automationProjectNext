import allure
from allure_commons.types import Severity

from pages.home_category_page import HomeCategory


class TestHomeCategory:
    @allure.severity(Severity.CRITICAL)
    @allure.description("Verify click on home category will open homeware page")
    @allure.title("open homeware page from homepage")
    def test_open_home_category(self):
        shopper = HomeCategory(self.driver)
        shopper.open_menu_category(shopper.HOME_CATEGORY_BTN)
        home_category_url = "https://www.next.co.il/en/homeware"
        current_url = self.driver.current_url
        assert current_url == home_category_url

