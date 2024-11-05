from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class HomeCategory(BasePage):
    THE_HOME_SHOP_BTN = (By.CSS_SELECTOR, "[data-ga-v3='THE HOME SHOP']")
    HOME_CATEGORY_BTN = (By.CSS_SELECTOR, "[data-title='HOME']")
    HOME_WARE_TITLE = (By.CSS_SELECTOR, ".font--weightBolder")
    LIVING_ROOM_SUBCATEGORY = (By.XPATH, "//a[@class='sidebar-links' and text()='Living Room']")
    LIVING_ROOM_SUBCATEGORY_TITLE = (By.XPATH, "//h1[text() = 'All Living Room']")
    PRODUCTS = (By.CSS_SELECTOR, ".produc-gzdrrz")
    SORT_LOW_TO_HIGH_PRODUCT1 = (By.CSS_SELECTOR, "[data-label='Orange Rosie Rabbit and Bertie Bear Halloween Pumpkin "
                                                  "Bathroom Door Sign']")
    SORT_LOW_TO_HIGH_PRODUCT2 = (By.CSS_SELECTOR, "[aria-label='Grey Chester The Cat Ring Holder ₪ 21']")
    ADD_PRODUCT_TO_FAVORITES_BTN = (By.CSS_SELECTOR, "[aria-label*='Add to Favourites']")
    ACTIVE_FAVORITE_BADGE = (By.CSS_SELECTOR, "[data-testid='header-fav-badge-active']")
    INACTIVE_FAVORITE_BADGE = (By.CSS_SELECTOR, "[data-testid='header-fav-badge-inactive']")
    REMOVE_PRODUCT_FROM_FAVORITES_BTN = (By.CSS_SELECTOR, "[data-testid='product-active-favourite-icon']")
    FIRST_HOMEWARE_BLUE_PRODUCT = (By.CSS_SELECTOR, ".produc-ivbv8a:first-of-type")
    FIRST_LIVING_ROOM_PRODUCT = (By.XPATH, "//p[contains(text(), 'Natural Wooden Global Pill Shelves')]")

    def __init__(self, driver):
        super().__init__(driver)

    def open_menu_category(self, category):
        self.click(category)
        self.click(self.THE_HOME_SHOP_BTN)

    def list_of_homeware_products(self):
        products = self.driver.find_elements(*self.PRODUCTS)
        return products

    def open_living_room_subcategory(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.HOME_CATEGORY_BTN))
        except TimeoutException:
            raise ValueError("Price element was not found or visible within the time limit.")
        self.open_menu_category(self.HOME_CATEGORY_BTN)
        self.click(self.LIVING_ROOM_SUBCATEGORY)
