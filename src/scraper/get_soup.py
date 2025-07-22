from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time


def get_soup(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")

    service = Service("D:/webdriver/chromedriver.exe", options=options)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    scroll_pause_time = 2
    last_height = driver.execute_script("return document.body.scrollHeight")

    for _ in range(20):
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(scroll_pause_time)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    html = driver.page_source
    driver.quit()
    return BeautifulSoup(html, "html.parser")
