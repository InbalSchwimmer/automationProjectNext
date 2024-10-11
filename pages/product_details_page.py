from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProductDetails(BasePage):
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".nowPrice")
    ADD_TO_BAG_FROM_FAVOURITE_BTN = (By.CSS_SELECTOR, ".add-to-bag")
    ADD_TO_BAG_BTN = (By.CSS_SELECTOR, ".nxbtn.primary.btn-addtobag.addToBagCTA")
    CONTINUE_AS_GUEST = (By.CSS_SELECTOR, "#Next")

    def __init__(self, driver):
        super().__init__(driver)

