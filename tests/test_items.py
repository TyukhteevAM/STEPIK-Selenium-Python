from selenium.webdriver.common.by import By


def test_check_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(5)
    trash_button_text = browser.find_element(By.CSS_SELECTOR,
                                             'button[class="btn btn-lg btn-primary btn-add-to-basket"]').text
    assert len(trash_button_text) > 0, "The trash button doesn't exist"
