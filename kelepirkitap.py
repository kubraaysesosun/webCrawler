import bs4
import requests



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

file = open("arama_gecmisi.txt", "a", encoding="utf-8")
keyword = input("Aramak istediğiniz kitap adı giriniz..")
file.write(",")
file.write(keyword)
file.close()

if __name__ == '__main__':
    kelepirkitap("küçük prens")