import time
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from data.locators import NextHomePageLocators


class NextHomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def change_shopping_country(self, location):
        self.click(NextHomePageLocators.COUNTRY_SELECTOR_BTN)
        self.click(NextHomePageLocators.LOCATION_DROPDOWN)
        self.click(location)
        self.click(NextHomePageLocators.COUNTRY_SELECTOR_ENGLISH_BTN)
        self.click(NextHomePageLocators.LOCATION_SHOP_NOW_BTN)
        time.sleep(10)

    def accept_all_cookies(self):
        try:
            # Wait for the button to be visible and clickable
            wait = WebDriverWait(self.driver, 15)
            wait.until(EC.element_to_be_clickable(NextHomePageLocators.ACCEPT_ALL_COOLIES_BTN))
            self.click(NextHomePageLocators.ACCEPT_ALL_COOLIES_BTN)
        except TimeoutException:
            print("Accept all cookies button did not appear within the timeout period.")
        except NoSuchElementException:
            print("Accept all cookies button does not exist on the page.")

    def continue_btn_after_country_change(self):
        try:
            # Wait for the button to be visible and clickable
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable(NextHomePageLocators.CONTINUE_BTN))
            self.click(NextHomePageLocators.CONTINUE_BTN)
        except NoSuchElementException:
            print("Continue Button does not exist on the page.")
