from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrome_driver_path = "C:\development\chromedriver.exe"

driver = webdriver.Chrome()

website = driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")
time.sleep(2)
add_cart = driver.find_element(By.XPATH, '//*[@id="add-to-cart-button"]')
add_cart.click()
time.sleep(10)
check_out = driver.find_element(By.XPATH, '//*[@id="sc-buy-box-ptc-button"]/span/input')
check_out.click()
time.sleep(10)
