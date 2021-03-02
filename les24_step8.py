from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
time.sleep(20)
price100 = WebDriverWait(browser, 12).until (
    EC.text_to_be_present_in_element ((By.ID, "price") , "100" )
)
if price100:
    browser.find_element_by_id("book").click()


x = int(browser.find_element_by_id("input_value").text)
def calc(x1):
    return math.log(abs(12*math.sin(x1)))
y = str(calc(x))
browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_tag_name("button[type=submit]").click()