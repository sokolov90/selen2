from selenium import webdriver
import os, time
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, "text.txt")

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("test-name")
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("test-lastname")
    input3 = browser.find_element_by_name("email")
    input3.send_keys("test-email")

    file1 = browser.find_element_by_id("file")
    file1.send_keys(file_path)

    browser.find_element_by_class_name("btn").click()

finally:
    time.sleep(10)
    browser.quit()