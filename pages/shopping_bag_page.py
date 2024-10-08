from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ShoppingBag(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    VIEW_EDIT_BAG_BTN = (By.CSS_SELECTOR, "[data-ga-v3='View Bag']")
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, ".dk_toggle.dk_label")
    REMOVE_ITEM_LINK = (By.XPATH, "//a[text() = 'Remove Item']")
    ITEM_COUNT = (By.CSS_SELECTOR, "#itemCount")
    ITEM_VALUE = (By.CSS_SELECTOR, "#sbtotals")
    ITEM_QUANTITY_TOGGLE = (By.CSS_SELECTOR, ".dk_toggle")
    # The locator is a template, and we'll replace '{}' with the actual quantity value dynamically
    ITEM_QUANTITY_SELECTOR_TEMPLATE = "[data-dk-dropdown-value='{}']"
    SHOP_MORE_LINK = (By.CSS_SELECTOR, "div.bottom a.shopmore")
    SAVE_FOR_LATER_LINK = (By.CSS_SELECTOR, ".btnSFL")
    SAVE_ITEM_COUNT = (By.CSS_SELECTOR, ".savedItemsCnt")

    def select_product_quantity(self, quantity):
        # Click the toggle to open the dropdown
        self.click(self.ITEM_QUANTITY_TOGGLE)

        # Dynamically create the locator by replacing '{}' with the actual quantity
        quantity_locator = (By.CSS_SELECTOR, self.ITEM_QUANTITY_SELECTOR_TEMPLATE.format(quantity))

        # Now click the specific quantity
        self.click(quantity_locator)
