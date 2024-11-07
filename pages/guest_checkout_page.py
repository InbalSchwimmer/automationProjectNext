import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from data.locators import GuestCheckoutLocators


class GuestCheckout(BasePage):
    # GUEST_TITLE_TF = (By.CSS_SELECTOR, "#Title")
    # MRS_TITLE = (By.CSS_SELECTOR, "[value='Mrs']")
    # FIRST_NAME_TF = (By.CSS_SELECTOR, "[name='FirstName']")
    # LAST_NAME_TF = (By.CSS_SELECTOR, "[name='LastName']")
    # EMAIL_TF = (By.CSS_SELECTOR, "[name='Email']")
    # PHONE_NUMBER_TF = (By.CSS_SELECTOR, "[name='PhoneNumber']")
    # ADDRESS_TF = (By.CSS_SELECTOR, "#AddressLine2")
    # CITY_TF = (By.CSS_SELECTOR, "#AddressLine4")
    # STATE_DROP_DOWN = (By.CSS_SELECTOR, "#AddressLine5")
    # ZIP_CODE_TF = (By.CSS_SELECTOR, "#AddressLine6")
    # PROVINCE_HAMERKAZ = (By.CSS_SELECTOR, "[value='HAMERKAZ']")
    # CONTINUE_BTN = (By.CSS_SELECTOR, "#SignupButton")
    # ERROR_EMAIL = (By.CSS_SELECTOR, "#Email-error")
    # NEXT_LOGO = (By.CSS_SELECTOR, "[data-ga='NEXT Home Page']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("guest details: {first_name}, {last_name}, {email}, {telephone}, {street}, {city}, {zip_code}")
    def fill_guest_info(self, first_name, last_name, email, telephone, street, city, zip_code):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(GuestCheckoutLocators.FIRST_NAME_TF)
        )
        self.fill_text(GuestCheckoutLocators.FIRST_NAME_TF, first_name)
        self.fill_text(GuestCheckoutLocators.LAST_NAME_TF, last_name)
        self.fill_text(GuestCheckoutLocators.EMAIL_TF, email)
        self.fill_text(GuestCheckoutLocators.PHONE_NUMBER_TF,telephone)
        self.fill_text(GuestCheckoutLocators.ADDRESS_TF, street)
        self.fill_text(GuestCheckoutLocators.CITY_TF, city)
        self.fill_text(GuestCheckoutLocators.ZIP_CODE_TF, zip_code)
