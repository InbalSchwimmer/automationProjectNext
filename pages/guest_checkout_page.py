import allure
from pages.base_page import BasePage
from data.locators import GuestCheckoutLocators


class GuestCheckout(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("guest details: {first_name}, {last_name}, {email}, {telephone}, {street}, {city}, {zip_code}")
    def fill_guest_info(self, first_name, last_name, email, telephone, street, city, zip_code):
        self.wait_for_element_visibility(GuestCheckoutLocators.FIRST_NAME_TF, timeout=20)
        self.fill_text(GuestCheckoutLocators.FIRST_NAME_TF, first_name)
        self.fill_text(GuestCheckoutLocators.LAST_NAME_TF, last_name)
        self.fill_text(GuestCheckoutLocators.EMAIL_TF, email)
        self.fill_text(GuestCheckoutLocators.PHONE_NUMBER_TF,telephone)
        self.fill_text(GuestCheckoutLocators.ADDRESS_TF, street)
        self.fill_text(GuestCheckoutLocators.CITY_TF, city)
        self.fill_text(GuestCheckoutLocators.ZIP_CODE_TF, zip_code)
