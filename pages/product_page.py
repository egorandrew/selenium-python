from selenium.common.exceptions import NoAlertPresentException  # в начале файла
from .base_page import BasePage
from .locators import BasketAddPageLocators
import math


class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*BasketAddPageLocators.ADD_IN_BASKET).click

