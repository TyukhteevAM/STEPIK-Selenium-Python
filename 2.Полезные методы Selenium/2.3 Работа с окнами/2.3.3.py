import time
from math import *

from selenium import webdriver
from selenium.webdriver.common.by import By
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, 'button.trollface').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_text = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    y = log(abs(12 * sin(x_text)))
    input_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_answer.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    alert = browser.switch_to.alert
    alert_text = alert.text
    print(alert_text.split(':')[1])
    confirm = browser.switch_to.alert
    confirm.accept()


finally:
    # успеваем скопировать код за 30 секунд
    # time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()