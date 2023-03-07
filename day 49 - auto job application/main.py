from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys # replicates key that's not letter, number or symbols, e.g. enter key
import time

USERNAME = "benjy.lovat@gmail.com"
PASSWORD = "3Ogk9FB88B1v7sszE8mYbI"

chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")
chrome_options.add_experimental_option("detach", True)
service = Service("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3488271893&f_AL=true&geoId=102257491&keywords=medical%20engineer&location=London%2C%20England%2C%20United%20Kingdom&refresh=true")
sign_in_button = driver.find_element(By.CLASS_NAME, "btn-secondary-emphasis")
sign_in_button.click()
# time.sleep(5)

username = driver.find_element(By.ID, "username")
username.send_keys(USERNAME)
password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
sign_in = driver.find_element(By.XPATH, "/html/body/div/main/div[3]/div[1]/form/div[3]/button")
sign_in.click()
time.sleep(5) # allows SSL handshake to go through so can find jobs

# Save all listings
jobs = driver.find_elements(By.CSS_SELECTOR, ".ember-view.jobs-search-results__list-item.occludable-update.p0.relative.scaffold-layout__list-item")
print([job.text for job in jobs])
time.sleep(2)
for job in jobs:
    print(job.text)
    job.click()
    time.sleep(2)
    if job.text != "":
        save = driver.find_element(By.CLASS_NAME, "jobs-save-button")
        save.click()
        time.sleep(2)
# driver.quit()