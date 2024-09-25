from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductDetails(BasePage):
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".nowPrice")

    def __init__(self, driver):
        super().__init__(driver)

    def get_price(self, price):
        return int(price.replace('₪', '').strip())  # return price in int
