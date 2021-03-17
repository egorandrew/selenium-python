from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import time


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    login_page = page.go_to_login_page()
    login_page.should_be_login_page()


def test_should_be_login(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_should_be_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login = LoginPage(browser, link)
    login.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    page = BasketPage(browser, link)
    page.empty_basket_message()
    page.empty_basket()
