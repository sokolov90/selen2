from selenium import webdriver
import time, math

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser.get(link)
    browser.find_element_by_tag_name("button").click()
    newwindow = browser.window_handles[1]
    oldwindow = browser.window_handles[0]
    browser.switch_to.window(newwindow)
    x = browser.find_element_by_id("input_value").text
    field = browser.find_element_by_name("text")
    field.send_keys(calc(x))
    browser.find_element_by_tag_name("button").click()
    answer = browser.switch_to.alert
    ans = answer.text
    answer.accept()
    print(ans)
finally:
    browser.quit()
