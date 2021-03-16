from .base_page import BasePage
from .locators import BasketAddPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*BasketAddPageLocators.ADD_IN_BASKET).click()

    def book_in_basket(self, name):
        assert name == self.browser.find_element(*BasketAddPageLocators.BOOK_NAME_ADD).text, "Товар не добавлен в " \
                                                                                             "корзину "

    def book_price(self, price):
        assert price == self.browser.find_element(*BasketAddPageLocators.BOOK_PRICE_ADD).text, "Стоимость корзины " \
                                                                                               "совпадает с ценой " \
                                                                                               "товара "

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *BasketAddPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(
            *BasketAddPageLocators.SUCCESS_MESSAGE), "Success message is disappeared, but should not be"
