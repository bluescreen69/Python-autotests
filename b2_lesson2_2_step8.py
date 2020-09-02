from selenium import webdriver
import time
import os 

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

input1 = browser.find_element_by_name("firstname")
input1.send_keys("Lila")
input2 = browser.find_element_by_name("lastname")
input2.send_keys("Turanga")
input3 = browser.find_element_by_name("email")
input3.send_keys("K-Pax")

file = browser.find_element_by_name("file")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
file.send_keys(file_path)

button = browser.find_element_by_css_selector("button.btn").click()

time.sleep(3)
browser.quit()