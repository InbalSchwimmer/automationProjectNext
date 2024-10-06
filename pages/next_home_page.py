import time

from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class NextHomePage(BasePage):
    COUNTRY_SELECTOR_BTN = (By.CSS_SELECTOR, "[data-testid='header-country-lang-flag']")
    LOCATION_DROPDOWN = (By.CSS_SELECTOR, "#mui-component-select-country-selector-select")
    LOCATION_SHOP_NOW_BTN = (By.XPATH, "//button[text() = 'SHOP NOW']")
    ISRAEL_LOCATION = (By.XPATH, "//img[@alt='IL']")
    IRELAND_LOCATION = (By.XPATH, "//img[@alt='IE'")
    IRELAND_LOCATION_OPTION = (By.CSS_SELECTOR, "[data-value='IE']")
    ISRAEL_LOCATION_OPTION = (By.CSS_SELECTOR, "[data-value='IL']")
    CONTINUE_BTN = (By.CSS_SELECTOR, "[data-testid='header-country-change-modal-confirm']")
    ACCEPT_ALL_COOLIES_BTN = (By.CSS_SELECTOR, "#onetrust-accept-btn-handler")
    CLOSE_COUNTRY_SELECTOR_WINDOW = (By.CSS_SELECTOR, "[data-testid='country-selector-close-button']")
    COUNTRY_SELECTOR_ENGLISH_BTN = (By.CSS_SELECTOR, "[data-ga-v3='English']")

    def __init__(self, driver):
        super().__init__(driver)

    def change_shopping_country(self, location):
        self.click(self.COUNTRY_SELECTOR_BTN)
        self.click(self.LOCATION_DROPDOWN)
        self.click(location)
        self.click(self.COUNTRY_SELECTOR_ENGLISH_BTN)
        self.click(self.LOCATION_SHOP_NOW_BTN)
        time.sleep(10)

    def accept_all_cookies(self):
        try:
            # Wait for the button to be visible and clickable
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable(self.ACCEPT_ALL_COOLIES_BTN))
            self.click(self.ACCEPT_ALL_COOLIES_BTN)
        except TimeoutException:
            print("Accept all cookies button did not appear within the timeout period.")
        except NoSuchElementException:
            print("Accept all cookies button does not exist on the page.")

    def continue_btn_after_country_change(self):
        try:
            # Wait for the button to be visible and clickable
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.element_to_be_clickable(self.CONTINUE_BTN))
            self.click(self.CONTINUE_BTN)
        except NoSuchElementException:
            print("Continue Button does not exist on the page.")
