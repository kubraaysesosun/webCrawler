import requests
import bs4

class kidega:
    def __init__(self,keyword):
        self.url="https://kidega.com/"
        self.keyword=keyword
        self.hdrs = {'User-Agent': 'Mozilla/5.0'}
        self.run()
    def run(self):

        r=requests.get(self.url+"arama?query="+self.keyword+"&order=fiyatArtan&minPrice=&maxPrice=")
        root_soup=bs4.BeautifulSoup(r.content,'html.parser')

        for i in root_soup.find_all("div",{"class":"newItem"}):
           for type in i.find_all("span",{"class":"icon-book"}):
                for link in i.select("a")[:1]:
                    print(link.get("href"))
file = open("arama_gecmisi.txt", "a", encoding="utf-8")
keyword=input("Aramak istediğiniz kitap adı giriniz..")
file.write(",")
file.write(keyword)
file.close()

if __name__ == '__main__':
    kidega("küçük prens")