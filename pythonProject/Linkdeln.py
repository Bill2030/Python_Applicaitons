import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
linkdeln_web = driver.get(url="https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

login = driver.find_element(By.LINK_TEXT, "Sign in")
login.click()
username = driver.find_element(By.ID, "username")
username.send_keys("benardbill@yahoo.co.uk")
password = driver.find_element(By.ID, "password")
password.send_keys("Today123")
password.send_keys(Keys.ENTER)
time.sleep(10)
#save jobs
save_job = driver.find_element(By.LINK_TEXT, "Save")
save_job.click()
