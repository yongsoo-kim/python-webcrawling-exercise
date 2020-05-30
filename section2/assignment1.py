import sys
import io
import urllib.request as req

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

url = "https://ssl.pstatic.net/tveta/libs/1289/1289403/d4250ec75d0f00b7c82d_20200521162149628.jpg"
savePath1="C:/Users/yongs/Documents/cm.jpg"

mem = req.urlopen(url).read()

with open(savePath1, 'wb') as saveFile1:
    saveFile1.write(mem)

print("check done")

