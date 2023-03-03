from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys # replicates key that's not letter, number or symbols, e.g. enter key

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_driver_path = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path, chrome_options=chrome_options)

driver.get("https://www.pythonanywhere.com/registration/register/beginner/")
user = driver.find_element(By.NAME, "username")
user.send_keys("test613")
email = driver.find_element(By.NAME, "email")
email.send_keys("jstew613@gmail.com")
pass1 = driver.find_element(By.NAME, "password1")
pass1.send_keys("@Tes2Pass!")
pass2 = driver.find_element(By.NAME, "password2")
pass2.send_keys("@Tes2Pass!")
checkbox = driver.find_element(By.NAME, "tos")
checkbox.click()
register = driver.find_element(By.ID, "id_register_button")
register.click()

