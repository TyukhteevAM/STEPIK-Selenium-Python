from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        get_url = self.browser.current_url
        assert "login" in get_url, "login is not in the URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "login form is not on the page"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "register form is not on the page"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REPEAT_PASSWORD_FIELD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()
