from selenium import webdriver
from selenium.webdriver.common.by import By
import time
TWITTER_USERNAME="Benbill18"
TWITTER_PASS="Bode153Wise261"

chrome_driver_path = "C:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
speed_web = driver.get(url= "https://twitter.com/")
time.sleep(10)
login_btn = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a/div/span/span')
login_btn.click()
time.sleep(10)
user_name = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
user_name.send_keys(TWITTER_USERNAME)
if user_name != TWITTER_USERNAME:
    click_next = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
    click_next.click()
else:
    print("That is the wrong username")
time.sleep(5)
user_password = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
user_password.send_keys(TWITTER_PASS)
user_login = driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
user_login.click()
time.sleep(10)
tweet = driver.find_element(By.XPATH, '<div data-offset-key="5fhjd-0-0" class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"><span data-offset-key="5fhjd-0-0"><br data-text="true"></span></div>')
tweet.send_keys("Its gonna be a good day today. .Tweet from my Robot Tweet. #100daysOfCode")
time.sleep(2)
submit_tweet = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/span/span')
submit_tweet.click()
time.sleep(40)


