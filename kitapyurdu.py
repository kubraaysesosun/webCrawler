import bs4
import requests


class kitapYurdu:
    def __init__(self, keyword):
        self.url = "https://kitapyurdu.com"
        self.keyword=keyword
        self.hdrs = {'User-Agent': 'Mozilla/5.0'}
        self.link=[]
        self.run()

    def run(self):
        #print(self.url + "/index.php?route=product/search&sort=rating &order=DESC&filter_name=" + self.keyword + "&filter_product_type=1&fuzzy=0")
        r = requests.get(self.url + "/index.php?route=product/search&filter_name=" + self.keyword)
        root_soup = bs4.BeautifulSoup(r.content, 'html.parser')
        for i in root_soup.find_all("a", {"itemprop": "url"}):
            link = i.get("href")
            file = open("item_links_kitapyurdu.txt", "a", encoding="utf-8")
            file.write(link)
            file.write(",")
            file.close()



"""file = open("arama_gecmisi.txt", "a", encoding="utf-8")
keyword=input("Aramak istediğiniz kitap adı giriniz..")
file.write(",")
file.write(keyword)
file.close()"""

if __name__ == '__main__':
    kitapYurdu("küçük prens")