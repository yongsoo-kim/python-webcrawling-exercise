from bs4 import BeautifulSoup
import urllib.request as req
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = "https://www.daum.net/"

html = req.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

# print("soup", soup)

news = soup.select("#news > div.news_prime > div > ul > li")

for i, e in enumerate(news, 1):
    print(i, ", ", e.find("a").string)
