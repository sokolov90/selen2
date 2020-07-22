from selenium import webdriver
import math, time

browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(calc(x))
    browser.find_element_by_id("robotCheckbox").click()
    browser.execute_script("window.scrollBy(0,200);")
    browser.find_element_by_id("robotsRule").click()
    browser.find_element_by_tag_name("button").click()
finally:
    time.sleep(10)
    browser.quit()
