from selenium.webdriver.common.by import By


class BasePageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini [href='/en-gb/basket/']")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BOOK_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")
    TEXT_ABOUT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGINPAGE_LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name = 'registration_submit']")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")


class MainPageLocators():
    pass


class ProductPageLocators():
    BOOK_NAME_IN_ALERT = (By.CSS_SELECTOR, "#messages > .alert-success strong")
    BOOK_NAME_IN_PRODUCTS = (By.CSS_SELECTOR, ".product_main > h1")
    BOOK_PRICE_IN_ALERT = (By.CSS_SELECTOR, "#messages > .alert-info strong")
    BOOK_PRICE_IN_PRODUCTS = (By.CSS_SELECTOR, ".product_main > .price_color")
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
