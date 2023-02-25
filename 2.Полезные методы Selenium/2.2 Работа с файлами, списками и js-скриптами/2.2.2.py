from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from math import *

link = "http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    y = log(abs(12*sin(x)))
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    # time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()