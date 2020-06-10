import sys
import io
import requests, json

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

res = requests.get("http://localhost:3000/shops")
res.raise_for_status()
if res.ok:
    data = res.json()
    print(data['shopInfo'])
    for d in data['shopInfo']:
        print(d['status'])


else:
    print("No...")

# print(r.text)
# print(r.raise_for_status())
# print(r.text)