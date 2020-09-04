from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGINPAGE_LINK = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_NAME_IN_PRODUCTS = (By.CSS_SELECTOR, ".product_main > h1")
    BOOK_NAME_IN_ALERT = (By.CSS_SELECTOR, "#messages > .alert-success strong")
    BOOK_PRICE_IN_PRODUCTS = (By.CSS_SELECTOR, ".product_main > .price_color")
    BOOK_PRICE_IN_ALERT = (By.CSS_SELECTOR, "#messages > .alert-info strong")