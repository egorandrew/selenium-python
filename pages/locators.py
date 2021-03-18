from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_VIEW = (By.XPATH, "//span/a[text()='Посмотреть корзину']")


class LoginPageLocators:
    LOGIN_PAGE = (By.XPATH, "//form[@id='login_form']")
    REGISTRATION_PAGE = (By.XPATH, "//form[@id='register_form']")
    REGISTRATION_EMAIL = (By.XPATH, "//input[@name='registration-email']")
    REGISTRATION_PASS1 = (By.XPATH, "//input[@name='registration-password1']")
    REGISTRATION_PASS2 = (By.XPATH, "//input[@name='registration-password2']")
    REGISTRATION_BUTTON = (By.XPATH, "//button[@name='registration_submit']")


class BasketAddPageLocators:
    BOOK_NAME = (By.XPATH, "//div/h1[contains(text(), '']")
    BOOK_NAME_ADD = (By.XPATH, "//div[@class='alertinner ']/strong")
    ADD_IN_BASKET = (By.XPATH, "//button[@value='Добавить в корзину']")
    BOOK_PRICE = (By.XPATH, '//div[@class=\'col-sm-6 product_main\']/p[@class=\'price_color\']')
    BOOK_PRICE_ADD = (By.XPATH, "//div[@class='alertinner ']/p/strong")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Ваша корзина удовлетворяет условиям')]")


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.XPATH, "//div/p[contains(text(), 'Ваша корзина пуста')]")
    PRODUCT_IN_BASKET = (By.XPATH, "//div/h2[contains(text(), 'Товары в корзине')]")

