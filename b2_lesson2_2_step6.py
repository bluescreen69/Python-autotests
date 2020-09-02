from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)

input = browser.find_element_by_id("answer").send_keys(y)

option1 = browser.find_element_by_id("robotCheckbox")
browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
option1.click()
option2 = browser.find_element_by_id("robotsRule").click()

button = browser.find_element_by_css_selector("button.btn").click()

time.sleep(3)
browser.quit()