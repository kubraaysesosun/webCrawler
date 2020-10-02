import bs4
import requests


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

file = open("arama_gecmisi.txt", "a", encoding="utf-8")
keyword=input("Aramak istediğiniz kitap adı giriniz..")
file.write(",")
file.write(keyword)
file.close()

if __name__ == '__main__':
    ucuzkitapal("küçük prens")