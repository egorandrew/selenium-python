from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), "Корзина не пуста, ожидаем пустую " \
                                                                                   "корзину"

    def empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Корзина не пуста, ожидаем " \
                                                                                  "уведомление пустой " \
                                                                                  "корзины"
