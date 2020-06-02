from bs4 import BeautifulSoup
import requests
import html5lib

res = requests.get("https://www.greaterkashmir.com/latest/page/1")
##print(res.text)

soup = BeautifulSoup(res.text,"html5lib")
news_list  = soup.find_all("div",class_="m-article-first-large-listing__inner")
news = news_list[0]
link = news.find("a")
time  = news.find(class_="entry-date published")
#print(news.text)
print(link.text) # Headline
print(link['href']) #  Link to text
print(time.text)