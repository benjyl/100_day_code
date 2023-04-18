from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys # replicates key that's not letter, number or symbols, e.g. enter key
from time import time
from bisect import bisect

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
driver.get("https://tinder.com/")
cookies = driver.find_element(By.XPATH, "//div[contains(text(), 'I decline')]").click()
login = driver.find_element(By.XPATH, "//div[contains(text(), 'Log in')]").click()
time.sleep(2)
google_login = driver.find_element(By.XPATH, "//div[contains(text(), 'Continue with Google')]").click()