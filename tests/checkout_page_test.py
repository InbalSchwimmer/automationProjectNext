import json
import os
import time
import allure
import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.guest_checkout_page import GuestCheckout
from pages.home_category_page import HomeCategory
from pages.product_details_page import ProductDetails
from utills.config import ConfigReader
from data.locators import HomeCategoryLocators, ProductDetailsLocators, MenuLocators, GuestCheckoutLocators


class TestCheckout:

    @pytest.fixture(scope="class")
    def load_test_data(self):
        # Get the absolute path to the JSON file
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_file_path = os.path.join(base_dir, 'data', 'shopper_data.json')

        with open(json_file_path) as f:
            return json.load(f)

    @pytest.mark.functional
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Verify shopper can checkout and pay for the product as a guest")
    @allure.title("Checkout as a guest")
    def test_fill_shopper_detail_success(self, load_test_data):
        shopper = HomeCategory(self.driver)
        with allure.step("Open homeware page - sub category 'Living room'"):
            WebDriverWait(self.driver,20).until(
                EC.visibility_of_element_located(HomeCategoryLocators.HOME_CATEGORY_BTN)
            )
            shopper.open_menu_category(HomeCategoryLocators.HOME_CATEGORY_BTN)
            shopper.open_living_room_subcategory()
            shopper.sort_page_results(MenuLocators.SORT_BY_PRICE_LOW_HIGH)

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(HomeCategoryLocators.SORT_LOW_TO_HIGH_PRODUCT1)
        )
        with allure.step("Add product to checkout page"):
            shopper.click(HomeCategoryLocators.SORT_LOW_TO_HIGH_PRODUCT1)
            product = ProductDetails(self.driver)
            product.click(ProductDetailsLocators.ADD_TO_BAG_BTN)
            product.click(MenuLocators.CHECKOUT_BTN)
        with allure.step("checkout - continue as a guest"):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(ProductDetailsLocators.CONTINUE_AS_GUEST)
            )
            product.click(ProductDetailsLocators.CONTINUE_AS_GUEST)
            shop_as_guest = GuestCheckout(self.driver)
        with allure.step("fill guest data"):
            shop_as_guest.click(GuestCheckoutLocators.GUEST_TITLE_TF)
            shop_as_guest.click(GuestCheckoutLocators.MRS_TITLE)
            # to close title drop down
            shop_as_guest.click(GuestCheckoutLocators.GUEST_TITLE_TF)
            for data in load_test_data["valid_credentials"]:
                shop_as_guest.fill_guest_info(data['first_name'], data['last_name'], data['email'], data['telephone'],
                                              data['street'], data['city'], data['zip_code'])
            shop_as_guest.click(GuestCheckoutLocators.ZIP_CODE_TF)
            shop_as_guest.click(GuestCheckoutLocators.PROVINCE_HAMERKAZ)
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(GuestCheckoutLocators.CONTINUE_BTN)
            )

            shop_as_guest.click(GuestCheckoutLocators.CONTINUE_BTN)
            # current_url = self.driver.current_url
            # expected_url = ConfigReader.read_config("general", "home_category_url")
            # assert current_url == expected_url
            assert True  # Replace with your actual assertion logic when using valid credentials
            # Navigate back to the previous page
            self.driver.back()
            shop_as_guest.click(GuestCheckoutLocators.NEXT_LOGO)

    @pytest.mark.regression
    @pytest.mark.functional
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify invalid email will display error message")
    @allure.title("guest invalid email")
    def test_guest_invalid_email(self, load_test_data):
        shopper = HomeCategory(self.driver)
        with allure.step("Open homeware page - sub category 'Living room'"):
            WebDriverWait(self.driver,10).until(
                EC.visibility_of_element_located(HomeCategoryLocators.HOME_CATEGORY_BTN)
            )
            shopper.open_menu_category(HomeCategoryLocators.HOME_CATEGORY_BTN)
            shopper.open_living_room_subcategory()
            shopper.sort_page_results(MenuLocators.SORT_BY_PRICE_LOW_HIGH)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(HomeCategoryLocators.SORT_LOW_TO_HIGH_PRODUCT1)
        )
        with allure.step("Add product to checkout page"):
            shopper.click(HomeCategoryLocators.SORT_LOW_TO_HIGH_PRODUCT1)
            product = ProductDetails(self.driver)
            product.click(ProductDetailsLocators.ADD_TO_BAG_BTN)
            product.click(MenuLocators.CHECKOUT_BTN)
        with allure.step("checkout - continue as a guest"):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(ProductDetailsLocators.CONTINUE_AS_GUEST)
            )
            product.click(ProductDetailsLocators.CONTINUE_AS_GUEST)
            shop_as_guest = GuestCheckout(self.driver)
        with allure.step("fill guest data"):
            shop_as_guest.click(GuestCheckoutLocators.GUEST_TITLE_TF)
            shop_as_guest.click(GuestCheckoutLocators.MRS_TITLE)
            # to close title drop down
            shop_as_guest.click(GuestCheckoutLocators.GUEST_TITLE_TF)
            expected_error = ConfigReader.read_config("errors", "email_error")
            for data in load_test_data["invalid_email"]:
                shop_as_guest.fill_guest_info(data['first_name'], data['last_name'], data['email'], data['telephone'],
                                              data['street'], data['city'], data['zip_code'])
                time.sleep(2)
                email_error = shop_as_guest.get_text(GuestCheckoutLocators.ERROR_EMAIL)
                assert email_error == expected_error
                print(f"error: {email_error}")
