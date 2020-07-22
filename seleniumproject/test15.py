from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:

    button1 = browser.find_element_by_id("book")

    check = WebDriverWait(browser, 10).until(
         EC.text_to_be_present_in_element((By.ID, "price"), ("100"))
    )
    button1.click()
#    browser.execute_script("window.scrollBy(0, 500);")


    x = browser.find_element_by_css_selector("#input_value").text
    print(x)
    field = browser.find_element_by_css_selector("#answer")
    field.send_keys(calc(x))
    submit = browser.find_element_by_id("solve")
    submit.click()
    ans = browser.switch_to.alert
    answer = ans.text
    print(answer)
    ans.accept()
finally:

    time.sleep(5)
    browser.quit()
