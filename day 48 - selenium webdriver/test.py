from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
 
service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.amazon.com/TCL-Class-720p-Smart-Roku/dp/B09YWT3P5Q/ref=sr_1_4?crid=1W3HPYTLCO930&keywords=tv&qid=1667902931&sprefix=tv%2Caps%2C348&sr=8-4")
price = driver.find_element(by=By.CLASS_NAME, value='a-offscreen').get_attribute("textContent")
price = float(price.split("$")[1])
print(price)