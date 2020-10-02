import pandas as pd
import requests
import bs4

import veritabani


class bkmkitap:
    def __init__(self,keyword):
        self.url="https://www.bkmkitap.com"
        self.keyword=keyword
        self.hdrs = {'User-Agent': 'Mozilla/5.0'}
        self.file = open("content.txt", "w", encoding="utf-8")
        self.run()

    def run(self):

        r=requests.get(self.url+"/arama?q="+self.keyword)
        print(self.url+"/search?q="+self.keyword+"&cat=0%2C10001&parentId=10001")
        root_soup=bs4.BeautifulSoup(r.content,'html.parser')

        link = []
        price = []
        name = []
        author = []

        for i in root_soup.find_all("div",{"class":"row"}):
            for i in root_soup.find_all("a", {"class": "fl col-12 text-description detailLink"}):

                print(i.get("title"))








if __name__ == '__main__':
        bkmkitap("küçük prens")
