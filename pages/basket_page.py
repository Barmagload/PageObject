from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_text_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_ABOUT_EMPTY_BASKET), \
            "No text about empty basket"

    def should_not_be_books_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BOOK_IN_BASKET), \
            "We have book(s) in basket, but we should not have"

