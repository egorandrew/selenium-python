from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_PAGE = (By.XPATH, "//form[@id='login_form']")
    REGISTRATION_PAGE = (By.XPATH, "//form[@id='register_form']")


class BasketAddPageLocators:
    BOOK_NAME = (By.XPATH, "//div/h1")
    BOOK_NAME_ADD = (By.XPATH, "//div[@class='alertinner ']/strong")
    ADD_IN_BASKET = (By.XPATH, "//button[@value='Добавить в корзину']")
    BOOK_PRICE = (By.XPATH, '//div[@class=\'col-sm-6 product_main\']/p[@class=\'price_color\']')
    BOOK_PRICE_ADD = (By.XPATH, "//div[@class='alertinner ']/p/strong")

