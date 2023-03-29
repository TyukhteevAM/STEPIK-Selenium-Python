from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6 >h1 ")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME_TO_THE_BASKET = (By.XPATH, "//div[@class='alertinner ']/strong")
    BASKET_PRICE = (By.XPATH, "//div[@class='alertinner ']/p[1]/strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")