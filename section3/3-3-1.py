import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

r = requests.get("https://api.github.com/events")
# or...r = requests.get("https://api.github.com/events", cookies={...})
# check error. Must be used for checking errors.
r.raise_for_status()
# print(r.text)

jar = requests.cookies.RequestsCookieJar()
jar.set("name", "kim", domain="httpbin.org", path="/cookies")

r2 = requests.get("http://httpbin.org/cookies", cookies=jar)
r2.raise_for_status()
print(r2.text)

# r3 = requests.get("https://github.com", timeout=3)
# print(r3.text)

r4 = requests.post("http://httpbin.org/post", data={"name": "kim"}, cookies=jar)
print(r4.text)

payload1 = {'key1': 'value1', 'key2': 'value2'}
payload2 = (('key1', 'value1'), ('key2', 'value2'))
payload3 = {'some': 'rice'}

# this will send as "form" data, not "json" data
r5 = requests.post('http://httpbin.org/post', data=payload1)
#r5 = requests.post('http://httpbin.org/post', data=payload2)
print(r5.text)

# Json needs to be serialized.
# this will send as "json" data, not "form" data
r6 = requests.post('http://httpbin.org/post', data=json.dumps(payload3))
print(r6.text)