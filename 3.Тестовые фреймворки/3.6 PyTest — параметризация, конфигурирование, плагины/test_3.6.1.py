from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as e_c
from selenium import webdriver
import time
import math
import pytest

# для старта pytest -v -s 3_6_3_step_OWLS_OvO.py
# s, чтоб видеть print
# v, для того, чтобы запустить расширенный визуальный режим

uncorrected_results = []

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    print("\nquit browser..")
    browser.quit()
    print(''.join(uncorrected_results))

@pytest.mark.parametrize('link_task', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_find_ufo(browser, link_task):
    link = f"https://stepik.org/lesson/{link_task}/step/1"
    browser.get(link)
    browser.implicitly_wait(55)
    browser.find_element(By.CSS_SELECTOR, 'a[href$="login"]').click()
    browser.find_element(By.CSS_SELECTOR, '#id_login_email').send_keys('***')
    browser.find_element(By.CSS_SELECTOR, '#id_login_password').send_keys('***')
    browser.find_element(By.XPATH, '//button[@class="sign-form__btn button_with-loader "]').click()
    time.sleep(3)
    answer_place = WebDriverWait(browser, 55) \
        .until(e_c.visibility_of_element_located((By.CSS_SELECTOR, '[placeholder="Напишите ваш ответ здесь..."]')))
    answer_place.send_keys(str(math.log(int(time.time()))))
    time.sleep(3)
    submit_button = WebDriverWait(browser, 55) \
        .until(e_c.visibility_of_element_located((By.CSS_SELECTOR, '[class="submit-submission"]')))
    submit_button.click()
    time.sleep(3)
    option_text = WebDriverWait(browser, 55) \
        .until(e_c.visibility_of_element_located((By.CSS_SELECTOR, '[class="smart-hints__hint"]'))).text
    time.sleep(3)
    # reset_button = WebDriverWait(browser, 55) \
    #     .until(e_c.visibility_of_element_located((By.CSS_SELECTOR, '[class="again-btn white"]')))
    # reset_button.click()
    # time.sleep(3)
    # ok_button = WebDriverWait(browser, 55) \
    #     .until(e_c.visibility_of_element_located((By.CSS_SELECTOR, '//*[text() = "OK"]')))
    # ok_button.click()

    if option_text != "Correct!":
        uncorrected_results.append(option_text)

    assert "Correct!" == option_text, f'Error: {option_text}'

    # The owls are not what they seem! OvO