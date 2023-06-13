from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_driver_path = "C:\development\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

website_html = driver.get("https://www.python.org")


soup = BeautifulSoup(website_html, "html.parser")


time.sleep(10)
