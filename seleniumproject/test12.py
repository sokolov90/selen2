from selenium import webdriver
import math, time

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    browser.find_element_by_class_name("btn").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element_by_id("input_value").text
    field = browser.find_element_by_id("answer")
    field.send_keys(calc(x))
    submit = browser.find_element_by_tag_name("button")
    submit.click()
    ans1 = browser.switch_to.alert
    ans = ans1.text
    print(ans)







finally:
    time.sleep(10)
    browser.quit()