from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
y_webpage = response.text

soup = BeautifulSoup(y_webpage, "html.parser")
article_tag = soup.find_all(class_="jsx-1913936986")
