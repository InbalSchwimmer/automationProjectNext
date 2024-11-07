from selenium.webdriver.common.by import By


class GuestCheckoutLocators:
    GUEST_TITLE_TF = (By.CSS_SELECTOR, "#Title")
    MRS_TITLE = (By.CSS_SELECTOR, "[value='Mrs']")
    FIRST_NAME_TF = (By.CSS_SELECTOR, "[name='FirstName']")
    LAST_NAME_TF = (By.CSS_SELECTOR, "[name='LastName']")
    EMAIL_TF = (By.CSS_SELECTOR, "[name='Email']")
    PHONE_NUMBER_TF = (By.CSS_SELECTOR, "[name='PhoneNumber']")
    ADDRESS_TF = (By.CSS_SELECTOR, "#AddressLine2")
    CITY_TF = (By.CSS_SELECTOR, "#AddressLine4")
    STATE_DROP_DOWN = (By.CSS_SELECTOR, "#AddressLine5")
    ZIP_CODE_TF = (By.CSS_SELECTOR, "#AddressLine6")
    PROVINCE_HAMERKAZ = (By.CSS_SELECTOR, "[value='HAMERKAZ']")
    CONTINUE_BTN = (By.CSS_SELECTOR, "#SignupButton")
    ERROR_EMAIL = (By.CSS_SELECTOR, "#Email-error")
    NEXT_LOGO = (By.CSS_SELECTOR, "[data-ga='NEXT Home Page']")


class HomeCategoryLocators:
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
    # FIRST_LIVING_ROOM_PRODUCT = (By.XPATH, "//p[contains(text(), 'Natural Wooden Global Pill Shelves')]")


class NextHomePageLocators:
    COUNTRY_SELECTOR_BTN = (By.CSS_SELECTOR, "[data-testid='header-country-lang-flag']")
    LOCATION_DROPDOWN = (By.CSS_SELECTOR, "#mui-component-select-country-selector-select")
    LOCATION_SHOP_NOW_BTN = (By.XPATH, "//button[text() = 'SHOP NOW']")
    ISRAEL_LOCATION = (By.XPATH, "//img[@alt='IL']")
    IRELAND_LOCATION = (By.XPATH, "//img[@alt='IE']")
    IRELAND_LOCATION_OPTION = (By.CSS_SELECTOR, "[data-value='IE']")
    ISRAEL_LOCATION_OPTION = (By.CSS_SELECTOR, "[data-value='IL']")
    CONTINUE_BTN = (By.CSS_SELECTOR, "[data-testid='header-country-change-modal-confirm']")
    ACCEPT_ALL_COOLIES_BTN = (By.XPATH, "//button[@id = 'onetrust-accept-btn-handler']")
    CLOSE_COUNTRY_SELECTOR_WINDOW = (By.CSS_SELECTOR, "[data-testid='country-selector-close-button']")
    COUNTRY_SELECTOR_ENGLISH_BTN = (By.CSS_SELECTOR, "[data-ga-v3='English']")


class ProductDetailsLocators:
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".nowPrice")
    ADD_TO_BAG_FROM_FAVOURITE_BTN = (By.CSS_SELECTOR, ".add-to-bag")
    ADD_TO_BAG_BTN = (By.CSS_SELECTOR, ".nxbtn.primary.btn-addtobag.addToBagCTA")
    CONTINUE_AS_GUEST = (By.CSS_SELECTOR, "#Next")


class ShoppingBagLocators:
    VIEW_EDIT_BAG_BTN = (By.CSS_SELECTOR, "[data-ga-v3='View Bag']")
    PRODUCT_QUANTITY = (By.CSS_SELECTOR, ".dk_toggle.dk_label")
    REMOVE_ITEM_LINK = (By.CSS_SELECTOR, ".sbm-idDeleteButton ")
    ITEM_COUNT = (By.CSS_SELECTOR, "#itemCount")
    EMPTY_CART_MSG = (By.CSS_SELECTOR, ".d-lg-block")
    ITEM_VALUE = (By.XPATH, "//div[@class ='sbm-order-total-price sbm-summary-price-value']")
    ITEM_QUANTITY_TOGGLE = (By.CSS_SELECTOR, ".dk_toggle")
    ITEM_QUANTITY_PLUS = (By.CSS_SELECTOR, ".qty-plus")
    # The locator is a template, and we'll replace '{}' with the actual quantity value dynamically
    ITEM_QUANTITY_SELECTOR_TEMPLATE = "[data-dk-dropdown-value='{}']"
    # SHOP_MORE_LINK = (By.CSS_SELECTOR, "div.bottom a.shopmore")
    SHOP_MORE_LINK = (By.CSS_SELECTOR, ".sbm-idShopMoreButton")
    SAVE_FOR_LATER_LINK = (By.CSS_SELECTOR, ".sbm-idSaveForLaterButton")
    SAVE_ITEM_COUNT = (By.CSS_SELECTOR, ".sfl-item-count")


class MenuLocators:
    CHECKOUT_BTN = (By.CSS_SELECTOR, "[data-ga-v2='Checkout']")
    SORT_BTN = (By.CSS_SELECTOR, "[data-testid='plp-desktop-sort-button']")
    SORT_BY_PRICE_LOW_HIGH = (By.CSS_SELECTOR, "[data-value='price']")
    FILTER_BY_COLOR_BTN = (By.CSS_SELECTOR, "[aria-label='Colour']")
    BLUE_CHECK_BOX = (By.CSS_SELECTOR, "[name='plp-facet-checkbox-colour:blue']")
    SHOPPING_BAG_BTN = (By.CSS_SELECTOR, "[data-testid='header-shopping-bag']")
    FAVORITES_BTN = (By.CSS_SELECTOR, ".favourites.header-ogfstg")
