import math
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def test_guest_can_add_product_to_basket(self):
        self.should_be_product_url()
        self.get_product_name()
        self.get_product_price()
        self.add_to_basket()
        self.solve_quiz_and_get_code()
        self.check_basket()

    def should_be_product_url(self):
        get_url = self.browser.current_url
        assert "?promo=newYear" in get_url, "'?promo=newYear' is not in the URL"

    def get_product_name(self):
        product_name = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(ProductPageLocators.PRODUCT_NAME)).text
        return product_name

    def get_product_price(self):
        product_price = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(ProductPageLocators.PRODUCT_PRICE)).text
        return product_price

    def add_to_basket(self):
        WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable(ProductPageLocators.ADD_TO_BASKET_BUTTON)).click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            # print(f"Your code: {alert_text}")
            alert.accept()
            # time.sleep(10000)
        except NoAlertPresentException:
            print("No second alert presented")

    def check_basket(self):
        product_name_text_to_the_basket = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable(ProductPageLocators.PRODUCT_NAME_TO_THE_BASKET)).text
        basket_price = WebDriverWait(self.browser, 20).until(
            EC.element_to_be_clickable(ProductPageLocators.BASKET_PRICE)).text
        assert product_name_text_to_the_basket == self.get_product_name(), "Wrong product in the basket"
        assert basket_price == self.get_product_price(), "Wrong price in the basket"
