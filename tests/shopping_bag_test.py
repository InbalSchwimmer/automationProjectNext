import time
import allure
from allure_commons.types import Severity
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.home_category_page import HomeCategory
from pages.product_details_page import ProductDetails
from pages.shopping_bag_page import ShoppingBag
from utills.config import ConfigReader


class TestShoppingBag:

    def add_product_to_shopping_bag_via_favorites(self):
        """Helper method to perform common steps for adding a product to the shopping bag."""
        shopper = HomeCategory(self.driver)
        shopper.open_living_room_subcategory()
        with allure.step("Add product to favorites page"):
            shopper.click(shopper.ADD_PRODUCT_TO_FAVORITES_BTN)
        with allure.step("Open favorites page"):
            shopper.click(shopper.FAVORITES_BTN)
        product = ProductDetails(self.driver)
        shopping_bag = ShoppingBag(self.driver)
        with allure.step("Add product to shopping bag"):
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(product.ADD_TO_BAG_FROM_FAVOURITE_BTN)
            )
            product.click(product.ADD_TO_BAG_FROM_FAVOURITE_BTN)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(shopping_bag.VIEW_EDIT_BAG_BTN)
        )
        shopping_bag.click(shopping_bag.VIEW_EDIT_BAG_BTN)
        return shopping_bag

    @allure.severity(Severity.CRITICAL)
    @allure.description("Verify click on add button will add product to shopping bag")
    @allure.title("Add product to shopping bag")
    def test_add_product_to_bag(self):
        shopping_bag = self.add_product_to_shopping_bag_via_favorites()
        with allure.step("Verify one product was added to the bag"):
            assert shopping_bag.get_text(shopping_bag.PRODUCT_QUANTITY) == "1"

    @allure.severity(Severity.CRITICAL)
    @allure.description("Verify click on remove button will remove product from shopping bag")
    @allure.title("Remove product from shopping bag")
    def test_remove_product_from_bag(self):
        shopping_bag = self.add_product_to_shopping_bag_via_favorites()
        with allure.step("Remove product from shopping bag"):
            shopping_bag.click(shopping_bag.REMOVE_ITEM_LINK)
        time.sleep(2)
        with allure.step("Verify product was removed from the bag"):
            assert shopping_bag.get_text(shopping_bag.ITEM_COUNT) == "0"

    @allure.severity(Severity.CRITICAL)
    @allure.description("Verify product value display matches the value displayed in the homeware page")
    @allure.title("Product value")
    def test_order_value(self):
        shopping_bag = self.add_product_to_shopping_bag_via_favorites()
        with allure.step("Verify product value displays correctly"):
            order_value = shopping_bag.get_price(shopping_bag.ITEM_VALUE)
            assert order_value == 159.0

    @allure.severity(Severity.CRITICAL)
    @allure.description("Verify item quantity can be changed and the price updates accordingly")
    @allure.title("Change product quantity")
    def test_change_item_quantity(self):
        shopping_bag = self.add_product_to_shopping_bag_via_favorites()
        with allure.step("Change product quantity from 1 to 2"):
            shopping_bag.select_product_quantity("2")
        with allure.step("Verify the total order value is correct"):
            order_value = shopping_bag.get_price(shopping_bag.ITEM_VALUE)
            assert order_value == 318.0

    @allure.severity(Severity.NORMAL)
    @allure.description("Verify clicking on Shop More link opens the Next home page")
    @allure.title("Continue shopping")
    def test_continue_shopping_link(self):
        shopping_bag = self.add_product_to_shopping_bag_via_favorites()
        with allure.step("Click on 'Shop more' link"):
            shopping_bag.click(shopping_bag.SHOP_MORE_LINK)
        with allure.step("Verify Next home page is displayed"):
            current_url = self.driver.current_url
            # get the expected url from config.ini
            expected_url = ConfigReader.read_config("general", "url")
            assert current_url == expected_url

    @allure.severity(Severity.NORMAL)
    @allure.description("Verify clicking on Save for later link saves the product")
    @allure.title("Save product for later")
    def test_save_product_for_later(self):
        shopping_bag = self.add_product_to_shopping_bag_via_favorites()
        with allure.step("Click on 'Save for later' link"):
            shopping_bag.click(shopping_bag.SAVE_FOR_LATER_LINK)
        with allure.step("Verify the product is moved to the saved items section"):
            time.sleep(3)
            assert shopping_bag.get_text(shopping_bag.SAVE_ITEM_COUNT) == "(1 item)"
