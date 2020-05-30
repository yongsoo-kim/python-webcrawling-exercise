import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

imgUrl="https://i.nhentai.net/galleries/1558799/14.jpg"
htmlURL="https://google.com"

savePath1="C:/Users/yongs/Documents/test1.jpg"
savePath2="C:/Users/yongs/Documents/index.html"


dw.urlretrieve(imgUrl, savePath1)
dw.urlretrieve(htmlURL, savePath2)

print("download done!")
