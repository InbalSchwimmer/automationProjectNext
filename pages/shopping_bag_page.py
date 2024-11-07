from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from data.locators import ShoppingBagLocators


class ShoppingBag(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def select_product_quantity(self, quantity):
        # Click the toggle to open the dropdown
        if ShoppingBagLocators.ITEM_QUANTITY_PLUS:
            self.click(ShoppingBagLocators.ITEM_QUANTITY_PLUS)
        else:
            self.click(ShoppingBagLocators.ITEM_QUANTITY_TOGGLE)
            # create locator by replacing '{}' with the actual quantity
            quantity_locator = (By.CSS_SELECTOR, ShoppingBagLocators.ITEM_QUANTITY_SELECTOR_TEMPLATE.format(quantity))
            # Now click the specific quantity
            self.click(quantity_locator)

