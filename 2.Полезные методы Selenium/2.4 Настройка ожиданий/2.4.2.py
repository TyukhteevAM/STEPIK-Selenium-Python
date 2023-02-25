import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import *

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'),'100'))
    button = browser.find_element(By.CSS_SELECTOR, "#book")
    button.click()
    time.sleep(2)
    x_text = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    print(x_text)
    y = log(abs(12 * sin(x_text)))
    input_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_answer.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "#solve")
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
