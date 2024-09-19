from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomeCategory(BasePage):
    THE_HOME_SHOP_BTN = (By.CSS_SELECTOR, "[data-ga-v3='THE HOME SHOP']")
    HOME_CATEGORY_BTN = (By.CSS_SELECTOR, "#meganav-link-6")
    HOME_WARE_TITLE = (By.CSS_SELECTOR, ".font--weightBolder")
    LIVING_ROOM_SUBCATEGORY = (By.CSS_SELECTOR, "#left-sidebar-links3-cfxmj7acyx4gwxvcha112psxr")

    def __init__(self, driver):
        super().__init__(driver)

    def open_menu_category(self, category):
        self.click(category)
        self.click(self.THE_HOME_SHOP_BTN)

