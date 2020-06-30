import sys
import io
import urllib.request as req
from bs4 import BeautifulSoup
import os.path  # For file path check

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# Download url
url = "https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename = "forecast.xml"

if not os.path.exists(savename):
    # If not exists, download it!
    req.urlretrieve(url, savename)

# BeautifulSoup parsing
xml = open(savename, 'r', encoding="utf-8").read()
soup = BeautifulSoup(xml, 'html.parser')  # XML is tag based one. so you can use this parser!

# Check locations first.
info = {}
for location in soup.find_all("location"):  # 'find' is much better than css or xpath, because xml files are 'tag' base.
    loc = location.find('city').string
    # print(loc)
    weather = location.find_all("tmn")
    # print(weather)
    if not (loc in info):  # key duplication check
        info[loc] = []
    for tmn in weather:
        info[loc].append(tmn.string)

print(info)
print(info.keys())  # get dictionary's keys only list
print(info.values())  # get dictionary's values only list

# Write weather text
with open('forecast-result.txt', 'wt', encoding='utf-8') as f:
    for loc in sorted(info.keys()):
        print("+", loc)
        f.write(str(loc) + '\n')
        for n in info[loc]:
            print("-", n)
            f.write('\t' + str(n) + '\n')
