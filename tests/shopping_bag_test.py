import time
import allure
import pytest
from allure_commons.types import Severity
from data.locators import HomeCategoryLocators, ProductDetailsLocators, ShoppingBagLocators, MenuLocators
from pages.home_category_page import HomeCategory
from pages.product_details_page import ProductDetails
from pages.shopping_bag_page import ShoppingBag
from utills.config import ConfigReader


class TestShoppingBag:

    def add_product_to_shopping_bag_via_favorites(self):
        """Helper method to perform common steps for adding a product to the shopping bag."""
        shopper = HomeCategory(self.driver)
        shopper.open_living_room_subcategory()
        with allure.step("Order by price - low to high"):
            shopper.sort_page_results(MenuLocators.SORT_BY_PRICE_LOW_HIGH)
        with allure.step("Add product to favorites page"):
            shopper.click(HomeCategoryLocators.ADD_PRODUCT_TO_FAVORITES_BTN)
        with allure.step("Open favorites page"):
            shopper.click(MenuLocators.FAVORITES_BTN)
        product = ProductDetails(self.driver)
        shopping_bag = ShoppingBag(self.driver)
        with allure.step("Add product to shopping bag"):
            shopping_bag.wait_for_element_visibility(ProductDetailsLocators.ADD_TO_BAG_FROM_FAVOURITE_BTN)
            product.click(ProductDetailsLocators.ADD_TO_BAG_FROM_FAVOURITE_BTN)
        shopping_bag.wait_for_element_visibility(ShoppingBagLocators.VIEW_EDIT_BAG_BTN)
        shopping_bag.click(ShoppingBagLocators.VIEW_EDIT_BAG_BTN)
        return shopping_bag

    @pytest.mark.regression
    @pytest.mark.functional
    @allure.severity(Severity.CRITICAL)
    @allure.description("Verify click on add button will add product to shopping bag")
    @allure.title("Add product to shopping bag")
    def test_add_product_to_bag(self):
        shopping_bag = self.add_product_to_shopping_bag_via_favorites()
        with allure.step("Verify one product was added to the bag"):
            assert shopping_bag.get_text(ShoppingBagLocators.PRODUCT_QUANTITY) in {"UK ONE", "One"}
        shopping_bag.click(ShoppingBagLocators.REMOVE_ITEM_LINK)

    @pytest.mark.regression
    @pytest.mark.functional
    @allure.severity(Severity.CRITICAL)
    @allure.description("Verify click on remove button will remove product from shopping bag")
    @allure.title("Remove product from shopping bag")
    def test_remove_product_from_bag(self):
        shopping_bag = self.add_product_to_shopping_bag_via_favorites()
        with allure.step("Remove product from shopping bag"):
            shopping_bag.click(ShoppingBagLocators.REMOVE_ITEM_LINK)
        time.sleep(2)
        with allure.step("Verify product was removed from the bag"):
            assert shopping_bag.get_text(ShoppingBagLocators.EMPTY_CART_MSG) in {"Your bag is empty"}

    @pytest.mark.regression
    @allure.severity(Severity.CRITICAL)
    @allure.description("Verify product value display matches the value displayed in the homeware page")
    @allure.title("Product value")
    def test_order_value(self):
        shopping_bag = self.add_product_to_shopping_bag_via_favorites()
        with allure.step("Verify product value displays correctly"):
            order_value = shopping_bag.get_price(ShoppingBagLocators.ITEM_VALUE)
            assert order_value == 18.0
        shopping_bag.click(ShoppingBagLocators.REMOVE_ITEM_LINK)

    @pytest.mark.regression
    @pytest.mark.functional
    @allure.severity(Severity.CRITICAL)
    @allure.description("Verify item quantity can be changed and the price updates accordingly")
    @allure.title("Change product quantity")
    def test_change_item_quantity(self):
        shopping_bag = self.add_product_to_shopping_bag_via_favorites()
        with allure.step("Change product quantity from 1 to 2"):
            shopping_bag.select_product_quantity("2")
        with allure.step("Verify the total order value is correct"):
            order_value = shopping_bag.get_price(ShoppingBagLocators.ITEM_VALUE)
            assert order_value == 36.0
        shopping_bag.click(ShoppingBagLocators.REMOVE_ITEM_LINK)

    @pytest.mark.regression
    @pytest.mark.functional
    @allure.severity(Severity.NORMAL)
    @allure.description("Verify clicking on Shop More link opens the Next home page")
    @allure.title("Continue shopping")
    def test_continue_shopping_link(self):
        shopping_bag = self.add_product_to_shopping_bag_via_favorites()
        with allure.step("Click on 'Shop more' link"):
            shopping_bag.click(ShoppingBagLocators.SHOP_MORE_LINK)
        with allure.step("Verify Next home page is displayed"):
            current_url = self.driver.current_url
            # get the expected url from config.ini
            expected_url = ConfigReader.read_config("general", "url")
            assert current_url.rstrip('/') == expected_url.rstrip('/')

    @pytest.mark.regression
    @pytest.mark.functional
    @allure.severity(Severity.NORMAL)
    @allure.description("Verify clicking on Save for later link saves the product")
    @allure.title("Save product for later")
    def test_save_product_for_later(self):
        shopping_bag = self.add_product_to_shopping_bag_via_favorites()
        with allure.step("Click on 'Save for later' link"):
            shopping_bag.click(ShoppingBagLocators.SAVE_FOR_LATER_LINK)
        with allure.step("Verify the product is moved to the saved items section"):
            time.sleep(3)
            assert shopping_bag.get_text(ShoppingBagLocators.SAVE_ITEM_COUNT) in {"(1 item)", "(1)"}
