from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys # replicates key that's not letter, number or symbols, e.g. enter key

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service("C:\Development\chromedriver.exe") # google chrome driver filepath
driver = webdriver.Chrome(service=service, chrome_options=chrome_options) 
driver.get("https://en.wikipedia.org/wiki/Main_Page")
# #articlecount as is an id and is the first anchortage in articlecount
article_count = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
print(article_count.text)
# article_count.click()

#find link by text between anchor tags
content_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# content_portals.click()

# insert info into input, typing instead of you
search = driver.find_element(By.NAME, "search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

driver.quit()