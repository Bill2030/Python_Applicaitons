import requests
from bs4 import BeautifulSoup

header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "Accept-Language":"en-US,en;q=0.9"
}

URL = "https://www.jumia.co.ke/tecno-spark-10-pro-6.8-256gb8gbdual-sim5000mahpearl-white-123172393.html"

response = requests.get(url=URL, headers=header)
jumia_web = response.content

soup = BeautifulSoup(jumia_web, "html.parser")
price = soup.find(class_= "-b -ltr -tal -fs24").get_text()
print(price)

price_without_symbol =price.split("KSh")[1]
print(price_without_symbol)
remove_comma = price_without_symbol.replace(",", "")
print(remove_comma)
price_as_float = float(remove_comma)
print(price_as_float)
