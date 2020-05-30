import sys
import io
import requests

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

#Open the session
s = requests.Session()


url1 = "https://www.naver.com"
#PUT(FETCH), DELETE. GET, POST
r1 = s.get(url1)

print('1', r1.text)

url2 = "http://httpbin.org/cookies"
r2 = s.get(url2, cookies={'from':'myName'})
print('1', r2.text)


url3 = "http://httpbin.org/get"
headers = {'user-agent':'myPython'}
r3 = s.get(url3, headers=headers)
print('1', r3.text)


#Close session
s.close()


with requests.Session() as s:
    r = s.get("http://www.naver.com")
    print(r.text)