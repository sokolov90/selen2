from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser.get(link)
    find1 = browser.find_element_by_id("treasure")
    x = find1.get_attribute("valuex")
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(calc(x))
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    button1 = browser.find_element_by_class_name("btn")
    button1.click()


finally:
    time.sleep(20)
    browser.quit()
