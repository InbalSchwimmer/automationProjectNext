import time

import allure
from allure_commons.types import Severity

from pages.next_home_page import NextHomePage


# @allure.description("Verify change Israel to Ireland country will saved")
# @allure.title("Open website from Israel - Israel flag displayed")
@allure.epic("User Interface and Navigation Testing")
@allure.feature("Homepage Functionality")
@allure.story("Verify core elements and user interactions on the homepage")
@allure.description("This scenario focuses on ensuring that the homepage displays correctly, with all essential "
                    "elements present and functional. It includes testing the visibility of the logo, navigation"
                    " menus, promotional banners, and call-to-action buttons. The goal is to ensure a seamless user"
                    "experience from the first interaction.")
class TestHomePage:
    @allure.severity(Severity.NORMAL)
    @allure.description("Verify Israel flag display in country selector")
    @allure.title("Open website from Israel - Israel flag displayed")
    def test_default_shopping_country(self):
        user = NextHomePage(self.driver)
        user.accept_all_cookies()
        assert user.ISRAEL_LOCATION

    @allure.severity(Severity.NORMAL)
    @allure.description("Verify change Israel to Ireland country will saved")
    @allure.title("Change shopping country flag")
    def test_country_selector(self):
        with allure.step("Change location to australia"):
            user = NextHomePage(self.driver)
            user.change_shopping_country(user.IRELAND_LOCATION_OPTION)
            user.accept_all_cookies()
            user.click(user.CLOSE_COUNTRY_SELECTOR_WINDOW)
            time.sleep(10)
            allure.attach(body=self.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.
                          attachment_type.PNG)
            assert user.IRELAND_LOCATION
            user.change_shopping_country(user.ISRAEL_LOCATION_OPTION)

    @allure.severity(Severity.BLOCKER)
    @allure.description("Verify checkout button displays")
    @allure.title("Checkout button exist")
    def test_checkout_btn(self):
        user = NextHomePage(self.driver)
        assert user.CHECKOUT_BTN




    # @allure.severity(Severity.BLOCKER)
    # @allure.description("Verify click on checkout button from home page will open checkout page")
    # @allure.title("Checkout button opens checkout page")
    # def test_checkout_functionality(self):
    #     user = HomePage(self.driver)
    #     user.click(user.CONTINUE_BTN)
    #     checkout_url = "https://account.next.co.il/en/login/Checkout"
    #     current_url = self.driver.current_url
    #     assert current_url == checkout_url
