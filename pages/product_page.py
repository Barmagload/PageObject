from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_equal_book_names(self):
        book_name_in_products = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_PRODUCTS).text
        book_name_in_alert = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_ALERT).text
        assert book_name_in_products == book_name_in_alert, "Book names in products and alert are not equal"

    def should_be_equal_book_names_and_book_prices(self):
        self.should_be_equal_book_names()
        self.should_be_equal_book_prices()

    def should_be_equal_book_prices(self):
        book_price_in_products = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_PRODUCTS).text
        book_price_in_alert = self.browser.find_element(*ProductPageLocators.BOOK_PRICE_IN_ALERT).text
        assert book_price_in_products == book_price_in_alert, "Book prices in products and alert are not equal"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Object is here, but should not bedisappeared"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

