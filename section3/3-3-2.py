import sys
import io
import requests, json


# Rest: POST, GET, PUT:UPDATE, REPLACE (FETCH: UPDATE, MODIFY), DELETE
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

payload1 = {'key1': 'value1', 'key2': 'value2'}
payload2 = (('key1', 'value1'), ('key2', 'value2'))
payload3 = {'some': 'rice'}


r1 = requests.put('http://httpbin.org/put', data=payload1)
print(r1.text)


r2 = requests.delete('http://httpbin.org/delete', data=payload1)
print(r2.text)

r3 = requests.put('http://jsonplaceholder.typicode.com/posts/1', data=payload1)
print(r3.text)


r4 = requests.delete('http://jsonplaceholder.typicode.com/posts/1')
print(r4.text)
