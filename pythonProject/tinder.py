from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "C:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
tinder_web = driver.get("https://tinder.com/")
login_page = driver.find_element(By.LINK_TEXT, "Log in")
login_page.click()
time.sleep(2)
login_with_facebook = driver.find_element(By.XPATH, '//*[@id="s-1156614029"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div')
login_with_facebook.click()
time.sleep(2)

