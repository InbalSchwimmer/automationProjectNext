import time

from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    CHECKOUT_BTN = (By.CSS_SELECTOR, "[data-ga-v2='Checkout']")
    SORT_BTN = (By.CSS_SELECTOR, "[data-testid='plp-desktop-sort-button']")
    SORT_BY_PRICE_LOW_HIGH = (By.CSS_SELECTOR, "[data-value='price']")
    FILTER_BY_COLOR_BTN = (By.CSS_SELECTOR,"[aria-label='Colour']")
    BLUE_CHECK_BOX = (By.CSS_SELECTOR, "[name='plp-facet-checkbox-colour:blue']")
    SHOPPING_BAG_BTN = (By.CSS_SELECTOR, "[data-testid='header-shopping-bag']")
    FAVORITES_BTN = (By.CSS_SELECTOR, ".favourites.header-ogfstg")

    def click(self, locator):
        time.sleep(1)
        self.driver.find_element(*locator).click()

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def fill_text(self, locator, text):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(text)

    def sort_page_results(self, locator):
        self.click(self.SORT_BTN)
        self.click(locator)

    # def choose_product_from_page_list(self, locator):
    #         products = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'produc-')]")
    #         return products[locator]
