from selenium.webdriver.common.by import By


class MainPageLocators:
    login_link = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    login_page = (By.XPATH, "//form[@id='login_form']")
    registration_page = (By.XPATH, "//form[@id='register_form']")

class BasketAddPage:
