import sys
import io
import urllib.request as req
from urllib.parse import urlencode

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

API = "https://api.ipify.org"

values = {
    'format': 'json'
}

print('before', values)
params = urlencode(values)
print('after', params)

url = API + "?" + params

print("URL", url)


reqData = req.urlopen(url).read().decode('utf-8')
print("output", reqData)

