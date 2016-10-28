#!/usr/bin/python
from __future__ import print_function
from sys import exit

try:
	from selenium import webdriver
	from pyvirtualdisplay import Display
except ImportError:
	print("\nError importing required modules\nPlease run dependencies.sh\n")
	exit(-1)
	
import time


display = Display(visible=0, size=(800, 500))
display.start()

browser = webdriver.Chrome()
time.sleep(1)
url = "http://172.16.166.10"

browser.get(url)
time.sleep(3)
uelement = browser.find_element_by_css_selector(".textfield2>input[type='text']")
pelement = browser.find_element_by_css_selector(".textfield2>input[type='password']")
lelement = browser.find_element_by_css_selector(".login2>input[type='image']")

uelement.click()
time.sleep(1)
uelement.send_keys("entry no.")  # Write your entry number instead of 14bcs027
time.sleep(1)
pelement.click()
time.sleep(1)
pelement.send_keys("password") # Write your password here instead of mine
time.sleep(1)
lelement.click()
time.sleep(3)

browser.close() # Remove this line, if you don't want browser to get closed after login process.

display.stop()
