from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductDetails(BasePage):
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".nowPrice")
    ADD_TO_BAG_BTN = (By.CSS_SELECTOR, ".add-to-bag")

    def __init__(self, driver):
        super().__init__(driver)

    def get_price(self, price):
        return int(price.replace('₪', '').strip())  # return price in int
