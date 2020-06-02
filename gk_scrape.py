from bs4 import BeautifulSoup
import requests
import html5lib
from csv import writer
# to find particular keywords in text (will use re later)
def match(text,keywords):
    for keyword in keywords:
        if keyword in text:
            return True
    
    return False


#The news pages
base_url = "https://www.greaterkashmir.com/latest/page/"

keywords=["internet","4G","2G","snapped","network","communication"]

##almost 1000 pages are present on gk website
for i in range(2,100):
    print("Scarping page : "+str(i))
    res = requests.get(base_url+str(i))
    ##print(res.text)

    soup = BeautifulSoup(res.text,"html5lib")
    #All divs containing news 
    news_list  = soup.find_all("div",class_="m-article-first-large-listing__inner")

    for news in news_list:
        headline = news.find("a").text
        link = news.find("a")['href']
        time  = news.find(class_="entry-date published").text

        #print(headline)
        #temp_link = "https://www.greaterkashmir.com/news/opinion/justice-running-on-2g/"
        news_text  = requests.get(link)
        soup_full = BeautifulSoup(news_text.text,"html5lib")

        #entire news story is container in multiple paragraphs , searching for keywords in each
        paras = soup_full.find_all("p")
        for para in paras:
            if para.text:
                if(match(str(para.text),keywords)):
                    print("-----------------------------------------")
                    print(headline)
                    print(time)
                    print(para.text)
                    print("----------------------------------------------")

                    with open("list.csv","w") as f:
                        csv_writer = writer(f)
                        csv_writer.writerow([headline,time,para.text])
                    break

        


        #print(news.text)
        # if match(str(link.text),keywords):
        #     print(link.text) # Headline
        #     #print(link['href']) #  Link to text
        #     print(time.text)


# temp_link = "https://www.greaterkashmir.com/news/opinion/justice-running-on-2g/"
# news_text  = requests.get(temp_link)
# soup_full = BeautifulSoup(news_text.text,"html5lib")
# paras = soup_full.find_all("p")
# for para in paras:
#     if para.text:
#         if(match(str(para.text),keywords)):
#             print(para.text)
#             break
