import simplejson as json
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# Dict(Json) declaration
data = {}
data['people'] = []
data['people'].append({
    'name': 'Kim',
    'website': 'naver.com',
    'from': 'Seoul'
})
data['people'].append({
    'name': 'Park',
    'website': 'google.com',
    'from': 'Busan'
})
data['people'].append({
    'name': 'Lee',
    'website': 'daum.net',
    'from': 'Incheon'
})

print(data)

# Dict(Json) -> Str (Serialization)
e = json.dumps(data, indent=2)
print(type(e))
print(e)

# Str -> Dick(Json) (Deserialization)
# With Dict, you can use Loop.
d = json.loads(e)
print(type(d))
print(d)

with open('member.json', 'w') as outfile:
    outfile.write(e)

with open('member.json', 'r') as infile:
    r = json.loads(infile.read())
    print("=======")
    print(type(r))
    print(r)
    for p in r['people']:
        print('Name: ' + p['name'])
        print('website: ' + p['website'])
        print('From: ' + p['from'])
