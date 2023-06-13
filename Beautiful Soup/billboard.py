from bs4 import BeautifulSoup
import requests
import time

URL = "https://www.billboard.com/charts/hot-100/2000-08-12"

response = requests.get(url=URL)
yc_website = response.text
soup = BeautifulSoup(yc_website, "html.parser")
music_list = soup.find_all(name = "h3", class_="a-no-trucate")
music_list_names = [song.getText().strip() for song in music_list]
print(music_list_names)

