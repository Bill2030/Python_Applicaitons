import smtplib

import requests
from bs4 import BeautifulSoup

MY_EMAIL="benardbiidocuments@gmail.com"
MY_PASS = "kyyrtedxdcobtlfw"

header = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9"
}

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

response = requests.get(url=URL, headers=header)
y_website = response.content

soup = BeautifulSoup(y_website,"lxml")
#print(soup.prettify())
price = soup.find(class_="a-offscreen").get_text()
print(price)
price_without_symbol = price.split("$")[1]
print(price_without_symbol)
price_as_float = float(price_without_symbol)
print(price_as_float)
if price_as_float < 100:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASS)
    connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg=f"subject: price drop \n"
                                                                   f"Please check on price drop from Amazon and buy the product")
