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
    'from': 'Seoul',
    'grade': [95, 77, 89, 91]
})
data['people'].append({
    'name': 'Park',
    'website': 'google.com',
    'from': 'Busan',
    'grade': [85, 67, 100, 93]
})
data['people'].append({
    'name': 'Lee',
    'website': 'daum.net',
    'from': 'Incheon',
    'grade': [98, 79, 99, 92]
})
#
# # Dict(Json) -> Str (Serialization)
# e = json.dumps(data, indent=2)
# print(type(e))
# print(e)
#
# # Str -> Dick(Json) (Deserialization)
# # With Dict, you can use Loop.
# d = json.loads(e)
# print(type(d))
# print(d)

# Json file write(dump)
with open('member2.json', 'w') as outfile:
    json.dump(data, outfile)

# Json file read(load)
with open('member2.json', 'r') as infile:
    r = json.load(infile)
    print(type(r))
    print(r)
    print("===================")
    for p in r['people']:
        print('Name: ' + p['name'])
        print('website: ' + p['website'])
        print('From: ' + p['from'])
        grade = ''
        for g in p['grade']:
            grade = grade + ' ' + str(g)
        print('Grade:', grade.lstrip())
        print('')
