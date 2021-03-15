from .base_page import BasePage
from .locators import BasketAddPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*BasketAddPageLocators.ADD_IN_BASKET).click()

    def book_in_basket(self):
        p1 = self.browser.find_element(*BasketAddPageLocators.BOOK_NAME).text
        print(p1)
        p2 = self.browser.find_element(*BasketAddPageLocators.BOOK_NAME_ADD).text
        print(p2)
        assert p1 == p2, "Товар не добавлен в корзину "

    def book_price(self):
        p1 = self.browser.find_element(*BasketAddPageLocators.BOOK_PRICE).text
        p2 = self.browser.find_element(*BasketAddPageLocators.BOOK_PRICE_ADD).text
        assert p1 == p2, "Стоимость корзины совпадает с ценой товара"
