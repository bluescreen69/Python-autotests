from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_css_selector("button.btn").click()
confirm = browser.switch_to.alert
confirm.accept()

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input = browser.find_element_by_id("answer").send_keys(y)

button2 = browser.find_element_by_css_selector("button.btn").click()

time.sleep(3)
browser.quit()
