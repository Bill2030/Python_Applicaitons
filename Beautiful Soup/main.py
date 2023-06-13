from bs4 import BeautifulSoup
import requests
import xlml

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
article_tag = soup.find(class_= "athing", id=36189962)
print(article_tag.getText())

article_score = soup.find_all(name="span", class_="score")
for score in article_score:
    score = score.getText()
    score_list = score.split()
    #print(score_list)
    numbers = score_list[0]
    print(numbers)
max_number = max(numbers)
print(max_number)

article_tag_all = soup.find_all(class_="athing")
#print(article_tag_all)
for tag in article_tag_all:
   tag_list = tag.getText()
   print(tag_list)








#with open("website.html", encoding="utf8")as file:
    #contents = file.read()

#soup = BeautifulSoup(contents, "html.parser")
#all_anchor_tags = soup.find_all(name = "a")
#print(all_anchor_tags)
#for tags in all_anchor_tags:
    #pass
#heading = soup.find(name="h1", id="name")
#print(heading.text)
#section_heading = soup.find(name="h3", class_="heading")
#print(section_heading.text)