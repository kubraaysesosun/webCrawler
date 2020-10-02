import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from kitapyurdu import kitapYurdu

class TwitterPosts:
    def __init__(self):
        self.url=""
        self.open_driver()

    def open_driver(self):
        driver = webdriver.Firefox()
        driver.get(self.url)
        time.sleep(3)


        driver.close()

if __name__ == '__main__':
    TwitterPosts()