import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    n1 = browser.find_element_by_id("num1").text
    n2 = browser.find_element_by_id("num2").text
    sum = int(n1) + int(n2)
    find3 = browser.find_element_by_id("dropdown")
    select1 = Select(find3)
    select1.select_by_visible_text(str(sum))
    browser.find_element_by_class_name("btn").click()

finally:
    time.sleep(10)
    browser.quit()

