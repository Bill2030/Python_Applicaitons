from bs4 import BeautifulSoup
import requests
from new import webdriver
from new.webdriver.common.by import By
from time import sleep

chrome_driver_path = "C:\development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

website_html = driver.get("https://www.python.org")

soup = BeautifulSoup(website_html, "html.parser")
print(soup.prettify())

sleep(5)
