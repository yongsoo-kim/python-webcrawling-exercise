import errno
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.parse as pas
import sys
import io
import os

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

keyword = input("Input the keyword for image search:")

base = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query="
quote = pas.quote_plus(keyword)
url = base + quote
res = req.urlopen(url).read()

save_path = "naver-image"
try:
    if not (os.path.isdir(save_path)):
        os.makedirs(os.path.join(save_path))
except OSError as e:
    if e.errno != errno.EEXIST:
        print("Failed at creating folder")
        raise


soup = BeautifulSoup(res, "html.parser")
img_list = soup.select("div.img_area > a.thumb._thumb > img")

#For now, we don't care about "user-agent"
for i, img in enumerate(img_list, 1):
    # print(img["data-source"])
    full_file_name = os.path.join(save_path, str(i)+'.jpg')
    req.urlretrieve(img['data-source'], full_file_name)


print("Download has been done!")