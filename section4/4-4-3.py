import urllib.request as req
import simplejson as json
import io
import sys
import os.path

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# url
url = "https://api.github.com/repositories"

# Save path and name
savename = "repo.json"
if not os.path.exists(url):
    req.urlretrieve(url, savename)

items = json.load(open(savename, 'r', encoding="utf-8"))
# itemsstr = json.loads(open(savename,'r',encoding='utf-8').read())


# Oupput
for item in items:
    print(item["full_name"] + "-" + item["owner"]["url"])
