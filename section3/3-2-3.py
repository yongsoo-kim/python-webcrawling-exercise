import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# Response status code.
s = requests.Session()

url1 = "http://httpbin.org/stream/20"
# get raw(byte) data. "stream" option will defer the download data and make you try more steps.
# https://requests.readthedocs.io/en/master/user/advanced/

r1 = s.get(url1, stream=True)
#print(r1.text)
print(r1.encoding)
#print(r1.json())

if r1.encoding is None:
    r1.encoding = 'utf-8'

for line in r1.iter_lines(decode_unicode=True):
    # print(line)
    b = json.loads(line) # Deserialize object to python data type -> Json to Dict.
    # print(type(b))
    # print(b['origin'])
    for e in b.keys():
        print("[key]:", e, "[values]:",b[e])


s.close()
