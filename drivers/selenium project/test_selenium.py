from selenium import webdriver;
from selenium.webdriver.common.keys import Keys; 
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import unittest
import logging
from random import randint
from selenium.common.exceptions import NoSuchElementException
driver = webdriver.Chrome(executable_path='./drivers/chromedriver')

driver.get("https://dsce-connect-website.vercel.app/index.html")
driver.maximize_window()
time.sleep(2)

a = ActionChains(driver)
m = driver.find_element_by_xpath("//a[normalize-space()='ABOUT']")
a.move_to_element(m).perform()
time.sleep(0.3)

n = driver.find_element_by_xpath("//a[normalize-space()='NOTICES']")
a.move_to_element(n).perform()
time.sleep(0.3)

o = driver.find_element_by_xpath("//a[normalize-space()='EVENTS']")
a.move_to_element(o).perform()
time.sleep(0.3)

p = driver.find_element_by_xpath("//a[normalize-space()='PROJECTS']")
a.move_to_element(p).perform()
time.sleep(0.3)

q = driver.find_element_by_xpath("//a[normalize-space()='PLACEMENTS']")
a.move_to_element(q).perform()
time.sleep(0.3)

r = driver.find_element_by_xpath("//a[normalize-space()='ACADEMICS']")
a.move_to_element(r).perform()
time.sleep(0.3)

s = driver.find_element_by_xpath("//a[normalize-space()='LOGIN']")
a.move_to_element(s).perform() 
time.sleep(0.3)

submit = driver.find_element_by_xpath("//a[normalize-space()='LOGIN']")
submit.click()

def slow_type(element: WebElement, text: str, delay: float=0.3):
    """Send a text to an element one character at a time with a delay."""
    for character in text:
        element.send_keys(character)
        time.sleep(delay)
username = driver.find_element_by_xpath("//input[@placeholder='Username']")        
text = "vinay"
slow_type(username, text)       

password = driver.find_element_by_xpath("//input[@placeholder='Password']")
text = "something"
slow_type(password, text)

time.sleep(0.5)

submit = driver.find_element_by_xpath("//input[@value='Login']")
submit.click()

time.sleep(3)

driver.quit()








