import time

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    CHECKOUT_BTN = (By.CSS_SELECTOR, "[data-ga-v2='Checkout']")

    def click(self, locator):
        time.sleep(1)
        self.driver.find_element(*locator).click()

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def fill_text(self, locator, text):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)
