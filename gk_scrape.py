from bs4 import BeautifulSoup
import requests
import html5lib

def match(text,keywords):
    for keyword in keywords:
        if keyword in text:
            return True
    
    return False

base_url = "https://www.greaterkashmir.com/latest/page/"
#keywords=["internet","2G","ban","snapped"]
keywords=["covid","COVID","covid19","covid-19","COVID-19"]
for i in range(1,10):
    print("Scarping page : "+str(i))
    res = requests.get(base_url+str(i))
    ##print(res.text)

    soup = BeautifulSoup(res.text,"html5lib")
    #All divs containing news 
    news_list  = soup.find_all("div",class_="m-article-first-large-listing__inner")

    for news in news_list:
        link = news.find("a")
        time  = news.find(class_="entry-date published")
        #print(news.text)
        if match(str(link.text),keywords):
            print(link.text) # Headline
            #print(link['href']) #  Link to text
            print(time.text)