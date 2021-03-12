from .base_page import BasePage
from .locators import BasketAddPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*BasketAddPageLocators.ADD_IN_BASKET).click

    def book_in_basket(self):
        name = self.browser.find_element()
