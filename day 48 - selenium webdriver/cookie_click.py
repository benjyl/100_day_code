from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys # replicates key that's not letter, number or symbols, e.g. enter key
from time import time
from bisect import bisect

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service("C:\Development\chromedriver.exe") # google chrome driver filepath
driver = webdriver.Chrome(service=service, chrome_options=chrome_options) 
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
start_time = time()
five_sec_start = start_time

def get_shop_options():
    """get shop items for clicking on and costs
    item cost increases every time by a new one

    Returns:
        list, list: list of shop items and costs
    """
    shop = driver.find_elements(By.CSS_SELECTOR, "#store div b")
    items = [item.text for item in shop]
    costs = []
    for item in items:
        split_item = item.split(" - ")
        # print(split_item)
        try:
            costs.append(int(split_item[1].replace(",", "")))
        except IndexError:
            pass
    return shop, costs


while time() - start_time < 50:
    while time() - five_sec_start <5:
        cookie.click()
    money = int(driver.find_element(By.ID, "money").text)
    shop, costs = get_shop_options()
    # print(costs)
    partition_index = bisect(costs, money)
    shop[partition_index-1].click()
    five_sec_start = time()

cookies_second = driver.find_element(By.ID, "cps").text
print(cookies_second)

driver.quit()