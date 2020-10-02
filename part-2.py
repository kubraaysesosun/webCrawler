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



class ucuzkitapal:
    def __init__(self, keyword):
        self.url = "https://www.ucuzkitapal.com/"
        self.keyword = keyword
        self.hdrs = {'User-Agent': 'Mozilla/5.0'}
        self.run()
    def run(self):
        count=0
        r = requests.get(self.url + "ara/?search_performed=Y&pcode=N&q="+self.keyword+"&security_hash=93458bb53d5a262703fb1a2c5d7256cf")
        root_soup = bs4.BeautifulSoup(r.content, 'html.parser')

        for i in root_soup.find_all("div", {"class": "ty-column4"}):
                for link in i.select("a")[:1]:
                    print(link.get("href"))
                    count+=1
        print(count)


class pandora:
    def __init__(self, keyword):
        self.url = "https://www.pandora.com.tr/"
        self.keyword = keyword
        self.hdrs = {'User-Agent': 'Mozilla/5.0'}
        self.run()
    def run(self):
        count=0
        r = requests.get(self.url + "Arama?text="+self.keyword+"&type=3&araButon=&sirala=5")
        root_soup = bs4.BeautifulSoup(r.content, 'html.parser')

        for i in root_soup.find_all("ul", {"id": "urunler"}):
                for link in i.select("a"):
                    print(link.get("href"))
                count+=1
        print(count)


class kelepirkitap:
    def __init__(self, keyword):
        self.url = "https://www.kelepirkitap.com/"
        self.keyword = keyword
        self.hdrs = {'User-Agent': 'Mozilla/5.0'}
        self.run()
    def run(self):
        count=0
        r = requests.get(self.url + "Arama?1&kelime="+self.keyword+"&sira=URUNFIYATIORJINAL&yon=ASC")
        root_soup = bs4.BeautifulSoup(r.content, 'html.parser')

        for i in root_soup.find_all("div", {"class": "productImage"}):
                link=i.find("a").get("href")
                print(link)
                count+=1
        print(count)


class yordamkitap:
    def __init__(self, keyword):
        self.url = "https://www.yordamkitap.com/"
        self.keyword = keyword
        self.hdrs = {'User-Agent': 'Mozilla/5.0'}
        self.run()
    def run(self):
        count=0
        r = requests.get(self.url + "index.php?p=Products&q_field_active=0&ctg_id=&q="+self.keyword+"&search=&q_field=")
        root_soup = bs4.BeautifulSoup(r.content, 'html.parser')

        for i in root_soup.find_all("div", {"class": "name"}):
                for link in i.select("a"):
                    print(self.url+link.get("href"))
                count+=1
        print(count)



file = open("arama_gecmisi.txt", "a", encoding="utf-8")
keyword=input("Aramak istediğiniz kitap adı giriniz..")
file.write(",")
file.write(keyword)
file.close()


if __name__ == '__main__':
        """kidega(keyword)
        ucuzkitapal(keyword)
        pandora(keyword)
        yordamkitap(keyword)"""
        kelepirkitap(keyword)