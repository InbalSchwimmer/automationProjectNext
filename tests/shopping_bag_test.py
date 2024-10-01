import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_category_page import HomeCategory
from pages.product_details_page import ProductDetails
from pages.shopping_bag_page import ShoppingBag


class TestShoppingBag:
    def test_add_two_product_to_bag(self):
        shopper = HomeCategory(self.driver)
        shopper.open_living_room_subcategory()
        shopper.click(shopper.ADD_PRODUCT_TO_FAVORITES_BTN)
        # shopper.click(shopper.ADD_PRODUCT_TO_FAVORITES_BTN)
        shopper.click(shopper.FAVORITES_BTN)
        product = ProductDetails(self.driver)
        shopping_bag = ShoppingBag(self.driver)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(product.ADD_TO_BAG_BTN))
        product.click(product.ADD_TO_BAG_BTN)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(shopping_bag.VIEW_EDIT_BAG_BTN))
        shopping_bag.click(shopping_bag.VIEW_EDIT_BAG_BTN)
        assert shopping_bag.get_text(shopping_bag.PRODUCT_QUANTITY) == "1"
