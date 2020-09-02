from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

x_element = browser.find_element_by_id("num1")
x = x_element.text
num1 = int(x)
y_element = browser.find_element_by_id("num2")
y = y_element.text
num2 = int(y)
sum = str(num1 + num2)


select = Select(browser.find_element_by_id("dropdown"))
select.select_by_value(sum)
time.sleep(1)

button = browser.find_element_by_css_selector("button.btn").click()

browser.quit()