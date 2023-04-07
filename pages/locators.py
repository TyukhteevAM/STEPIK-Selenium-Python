from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group>a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    REPEAT_PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password2")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6 >h1 ")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME_TO_THE_BASKET = (By.XPATH, "//div[@class='alertinner ']/strong")
    BASKET_PRICE = (By.XPATH, "//div[@class='alertinner ']/p[1]/strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")


class BasketPageLocators:
    ITEMS_CONTAINER = (By.CSS_SELECTOR, "#basket_formset")
    NO_ITEMS_TEXT = (By.CSS_SELECTOR, "#content_inner")
