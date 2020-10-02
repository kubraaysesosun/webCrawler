import bs4
import requests




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
    yordamkitap("küçük prens")