import requests
import bs4

class kitapYurdu:
    def __init__(self, keyword):
        self.url = "https://kitapyurdu.com"
        self.keyword=keyword
        self.hdrs = {'User-Agent': 'Mozilla/5.0'}
        self.link=[]
        self.run()

    def run(self):
        print(self.url+"/index.php?route=product/search&sort=rating &order=DESC&filter_name="+self.keyword+"&filter_product_type=1&fuzzy=0")
        r = requests.get(self.url + "/index.php?route=product/search&filter_name=" + self.keyword)
        root_soup = bs4.BeautifulSoup(r.content, 'html.parser')
        for i in root_soup.find_all("a",{"itemprop":"url"}):
            link=i.get("href")
            self.link.append(link)
            print(link)


class idefix:
    def __init__(self,keyword):
        self.url="https://www.idefix.com"
        self.keyword=keyword
        self.hdrs = {'User-Agent': 'Mozilla/5.0'}
        self.run()
    def run(self):
        r = requests.get(self.url + "/search/?ActiveCategoryId=11693&Q=" + self.keyword)
        root_soup = bs4.BeautifulSoup(r.content, 'html.parser')
        for info in root_soup.find_all("div",{"class":"product-info"}) :
            print(info.text)







class bkmkitap:
    def __init__(self,keyword):
        self.url="https://www.bkmkitap.com"
        self.keyword=keyword
        self.hdrs = {'User-Agent': 'Mozilla/5.0'}
        self.run()
    def run(self):

        r=requests.get(self.url+"/arama?q="+self.keyword)
        print(self.url+"/search?q="+self.keyword+"&cat=0%2C10001&parentId=10001")
        root_soup=bs4.BeautifulSoup(r.content,'html.parser')
        for i in root_soup.find_all("a",{"class":"image-wrapper"}):
            print(self.url+i.get("href"))


"""file = open("arama_gecmisi.txt", "a", encoding="utf-8")
keyword=input("Aramak istediğiniz kitap adı giriniz..")
file.write(",")
file.write(keyword)
file.close()"""

if __name__ == '__main__':
    idefix("küçük prens")
