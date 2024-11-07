from pages.base_page import BasePage
from data.locators import HomeCategoryLocators


class HomeCategory(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def open_menu_category(self, category):
        self.click(category)
        self.click(HomeCategoryLocators.THE_HOME_SHOP_BTN)

    def list_of_homeware_products(self):
        products = self.driver.find_elements(*HomeCategoryLocators.PRODUCTS)
        return products

    def open_living_room_subcategory(self):
        self.wait_for_element_visibility(HomeCategoryLocators.HOME_CATEGORY_BTN)
        self.open_menu_category(HomeCategoryLocators.HOME_CATEGORY_BTN)
        self.click(HomeCategoryLocators.LIVING_ROOM_SUBCATEGORY)
