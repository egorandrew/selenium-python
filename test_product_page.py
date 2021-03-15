from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket1(browser):
    name = "The shellcoder's handbook"
    price = "9,99 £"
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.book_in_basket(name)
    page.book_price(price)

def test_guest_can_add_product_to_basket2(browser):
    name = "Coders at Work"
    price = "19,99 £"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019."
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.book_in_basket(name)
    page.book_price(price)
