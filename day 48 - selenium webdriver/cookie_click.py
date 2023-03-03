from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys # replicates key that's not letter, number or symbols, e.g. enter key
from time import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service("C:\Development\chromedriver.exe") # google chrome driver filepath
driver = webdriver.Chrome(service=service, chrome_options=chrome_options) 
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
start_time = time()
five_sec_start = start_time

while time() - start_time < 300:
    while time() - five_sec_start <5:
        cookie.click()
    five_sec_start = time()
