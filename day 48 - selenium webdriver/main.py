from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\Development\chromedriver.exe" # allows selenium use with chrome
# service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=Service(chrome_driver_path)) # google chrome

# driver.get("https://www.amazon.co.uk/Wahoo-Cadence-Sensor-Android-Computers/dp/B00L9XNFPY/ref=sr_1_1_sspa?keywords=wahoo%2Bcadence%2Bsensor&qid=1677765005&sprefix=wahoo%2Bcade%2Caps%2C66&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")
# cost = driver.find_element(by=By.CLASS_NAME, value="a-offscreen").get_attribute("textContent") # gets product cost
# # cost = float(cost.split("£")[1])
# print(cost)
# # print(cost.get_attribute("value"))
# driver.close() # closes active tab


# driver.get("https://www.python.org/")
# documentation_link = driver.find_element(by=By.CSS_SELECTOR, value=".documentation-widget a") # find anchortag "a" within _ documentation widget class (.docum... is to include all before it seems)  
# print(documentation_link.text)

# Challenge: Find dates and names of upcoming events on python homepage, create dict
driver.get("https://www.python.org/")
# find time element inside the medium-widget event widget, replace spaces by dot, looking for time tag
event_dates = driver.find_elements(by=By.CSS_SELECTOR, value=".medium-widget.event-widget.last time")

#method 1: using xpath containing partial href
# event_names = driver.find_elements(by=By.XPATH, value="//a[contains(@href, 'python-user-group/')]") # value in this format allows finding anchor tag containing partial href

#method 2 (cleaner): using css_selector, if only use the anchortag search inside event-widget will get the "more" button too 
# more button is nested inside paragraph but events are inside list so can search for an "a" inside a "li"
# space between each tag go deeper in to
event_names = driver.find_elements(by=By.CSS_SELECTOR, value=".medium-widget.event-widget.last li a")

event_dates = [date.text for date in event_dates]
event_names = [name.text for name in event_names if name.text] # only keep event name elements that are not empty
print(event_names)
driver.quit() # quits entire browser 
data = {i: {"time": event_dates[i], "name": event_names[i]} for i in range(len(event_dates))}
print(data)