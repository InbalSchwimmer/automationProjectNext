from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ShoppingBag(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    VIEW_EDIT_BAG_BTN = (By.CSS_SELECTOR, "[data-ga-v3='View Bag']")
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, ".dk_toggle.dk_label")
