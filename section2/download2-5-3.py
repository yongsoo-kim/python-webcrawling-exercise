from bs4 import BeautifulSoup
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

html = """
<html><body>
  <ul>
    <li><a href="http://www.naver.com">naver</a></li>
    <li><a href="http://www.daum.net">daum</a></li>
    <li><a href="https://www.google.com">google</a></li>
    <li><a href="https://www.tistory.com">tistory</a></li>
  </ul>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

#Tag selector

links = soup.find_all("a")
# or you can add condition for selecting particular tag.
# a = soup.find_all("a", string="daum")
# print("a",type(a), a)
b = soup.find_all("a", limit=3)
c = soup.find_all(string=["naver", "google"])
print(b)
print(c)

# links <class 'bs4.element.ResultSet'>
print('links', type(links))

for a in  links:
    # print('a', type(a), a)
    href = a.attrs['href']
    txt = a.string
    print('txt >> ', txt, 'href >> ', href)
