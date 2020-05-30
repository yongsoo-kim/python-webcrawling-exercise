import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# Response status code.
s = requests.Session()

url1 = "http://httpbin.org/get"
r1 = s.get(url1)
print(r1.status_code)
print(r1.ok)

#Json test site
#https://jsonplaceholder.typicode.com

url2 = "http://jsonplaceholder.typicode.com/posts/1"
r2 = s.get(url2)
print(r2.text)
print(r2.json()) # only for 'requests' module
print(r2.json().keys())
print(r2.json().values())
print(r2.encoding)
print(r2.content)
print(r2.raw)




s.close()
