from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    element = browser.find_element_by_id("price")
    x = element.text

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '$100'))

    button = browser.find_element_by_css_selector("#book")
    button.click()

    x_element = browser.find_element_by_css_selector("#input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_name("text")
    input1.send_keys(y)

    button1 = browser.find_element_by_id("solve")
    button1.click()
finally:


    time.sleep(10)
    browser.quit()
