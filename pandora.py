import bs4
import requests


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


file = open("arama_gecmisi.txt", "a", encoding="utf-8")
keyword=input("Aramak istediğiniz kitap adı giriniz..")
file.write(",")
file.write(keyword)
file.close()

if __name__ == '__main__':
    pandora("küçük prens")