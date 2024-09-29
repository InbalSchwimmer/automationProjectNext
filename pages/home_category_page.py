from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomeCategory(BasePage):
    THE_HOME_SHOP_BTN = (By.CSS_SELECTOR, "[data-ga-v3='THE HOME SHOP']")
    HOME_CATEGORY_BTN = (By.CSS_SELECTOR, "#meganav-link-6")
    HOME_WARE_TITLE = (By.CSS_SELECTOR, ".font--weightBolder")
    LIVING_ROOM_SUBCATEGORY = (By.XPATH, "//a[@class='sidebar-links' and text()='Living Room']")
    LIVING_ROOM_SUBCATEGORY_TITLE = (By.XPATH, "//h1[text() = 'All Living Room']")
    # PRODUCTS = (By.XPATH, "//div[contains(@class, 'produc-')]")
    PRODUCTS = (By.CSS_SELECTOR, ".produc-gzdrrz")
    SORT_LOW_TO_HIGH_PRODUCT1 = (By.CSS_SELECTOR, "[aria-label='Orange Pumpkin Halloween Bathroom Door Sign ₪ 18']")
    SORT_LOW_TO_HIGH_PRODUCT2 = (By.CSS_SELECTOR, "[aria-label='Grey Chester The Cat Ring Holder ₪ 21']")
    ADD_PRODUCT_TO_FAVORITES_BTN = (By.CSS_SELECTOR, "[aria-label*='Add to Favourites']")
    ACTIVE_FAVORITE_BADGE = (By.CSS_SELECTOR, "[data-testid='header-fav-badge-active']")
    INACTIVE_FAVORITE_BADGE = (By.CSS_SELECTOR, "[data-testid='header-fav-badge-inactive']")
    REMOVE_PRODUCT_FROM_FAVORITES_BTN = (By.CSS_SELECTOR, "[data-testid='product-active-favourite-icon']")
    FIRST_HOMEWARE_BLUE_PRODUCT = (By.CSS_SELECTOR, ".produc-ivbv8a:first-of-type")

    def __init__(self, driver):
        super().__init__(driver)

    def open_menu_category(self, category):
        self.click(category)
        self.click(self.THE_HOME_SHOP_BTN)

    def list_of_homeware_products(self):
        products = self.driver.find_elements(*self.PRODUCTS)
        return products

    def open_living_room_subcategory(self):
        self.open_menu_category(self.HOME_CATEGORY_BTN)
        self.click(self.LIVING_ROOM_SUBCATEGORY)
