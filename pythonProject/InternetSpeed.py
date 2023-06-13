import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "benardbill@yahoo.co.uk"
TWITTER_PASS = "Bode153Wise261"

chrome_driver_path = "C:\development\chromedriver.exe"

class InternetSpeedTwitterBot:
    def __init__(self, down, up, driver):
        self.down = down
        self.up = up
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        # Depending on your location, you might need to accept the GDPR pop-up.
        # accept_button = self.driver.find_element_by_id("_evidon-banner-acceptbutton")
        # accept_button.click()

        time.sleep(3)
        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()

        time.sleep(60)
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text


def tweet_at_provider(self):
    self.driver.get("https://twitter.com/login")

    time.sleep(2)
    email = self.driver.find_element_by_xpath(
        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
    password = self.driver.find_element_by_xpath(
        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

    email.send_keys("Benbill18")
    password.send_keys("Bode153Wise261")
    time.sleep(2)
    password.send_keys(Keys.ENTER)

    time.sleep(5)
    tweet_compose = self.driver.find_element_by_xpath(
        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

    tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
    tweet_compose.send_keys(tweet)
    time.sleep(3)

    tweet_button = self.driver.find_element_by_xpath(
        '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
    tweet_button.click()

    time.sleep(2)
    self.driver.quit()

bot = InternetSpeedTwitterBot(chrome_driver_path)
bot.get_internet_speed()
bot.tweet_at_provider()



        



