import requests
import bs4
import veritabani
import pandas as pd


class idefix:
    def __init__(self,keyword):
        self.url="https://www.idefix.com"
        self.keyword=keyword
        self.hdrs = {'User-Agent': 'Mozilla/5.0'}
        self.file = open("content.txt", "w", encoding="utf-8")
        self.run()
    def run(self):
        r = requests.get(self.url + "/search/?ActiveCategoryId=11693&Q=" + self.keyword)
        root_soup = bs4.BeautifulSoup(r.content, 'html.parser')
        link = []
        price=[]
        name=[]
        author=[]
        for i in root_soup.find_all("div",{"class":"cart-product-box-view"}):

            for z in i.find_all("a",{"style":"box-shadow: none;"}):
                name.append(z.get("title"))
                link.append(self.url+z.get("href"))

        for i in root_soup.find_all("div",{"class":"box-line-4"}):
            for x in i.find_all("span",{"id":"prices"}):
                y=x.text
                price.append(y)
        for i in root_soup.find_all("div",{"class":"box-line-2 pName"}):
            author.append(i.text)


        d={'name':name,'link':link,'author':author,'price': price}

        df=pd.DataFrame(data=d)

        for i in range(0,len(df)):
            veritabani.veri_ekle(df['name'][i],df['link'][i],df['author'][i],df['price'][i])



if __name__=="__main__":
    idefix("satranç")