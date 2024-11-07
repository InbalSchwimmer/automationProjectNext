import time
import allure
import pytest
from allure_commons.types import Severity
from pages.next_home_page import NextHomePage
from utills.config import ConfigReader
from data.locators import NextHomePageLocators


@allure.epic("User Interface and Navigation Testing")
@allure.feature("Homepage Functionality")
@allure.story("Verify core elements and user interactions on the homepage")
@allure.description("This scenario focuses on ensuring that the homepage displays correctly, with all essential "
                    "elements present and functional. It includes testing the visibility of the logo, navigation"
                    " menus, promotional banners, and call-to-action buttons. The goal is to ensure a seamless user"
                    "experience from the first interaction.")
class TestHomePage:
    @pytest.mark.regression
    @pytest.mark.functional
    @allure.severity(Severity.NORMAL)
    @allure.description("Verify Israel flag display in country selector")
    @allure.title("Open website from Israel - Israel flag displayed")
    def test_default_shopping_country(self):
        user = NextHomePage(self.driver)
        user.accept_all_cookies()
        with allure.step("Verify Israel flag display in right hand side country selector"):
            assert user.element_exist(NextHomePageLocators.ISRAEL_LOCATION)

    @pytest.mark.regression
    @pytest.mark.functional
    @allure.severity(Severity.NORMAL)
    @allure.description("Verify change Israel to Ireland country will saved")
    @allure.title("Change shopping country flag")
    def test_country_selector(self):
        self.driver.refresh()
        with allure.step("Change location to Ireland"):
            user = NextHomePage(self.driver)
        with allure.step("Open window for change shopper country and change it to Ireland"):
            user.change_shopping_country(NextHomePageLocators.IRELAND_LOCATION_OPTION)
        with allure.step("Accept all coolies"):
            user.accept_all_cookies()
        with allure.step("Close change shopper country window"):
            user.click(NextHomePageLocators.CLOSE_COUNTRY_SELECTOR_WINDOW)
            time.sleep(10)
            allure.attach(body=self.driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.
                          attachment_type.PNG)
        with allure.step("Verify Ireland flag display"):
            assert user.element_exist(NextHomePageLocators.IRELAND_LOCATION)
        user.change_shopping_country(NextHomePageLocators.ISRAEL_LOCATION_OPTION)
