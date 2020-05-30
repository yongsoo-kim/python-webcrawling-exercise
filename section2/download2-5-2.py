from bs4 import BeautifulSoup
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

html = """
<html>
<body>
<h1> Python Beatiful soup study</h1>
<p>Tag selector</p>
<p>CSS selector</p>
</body>
</html>
"""



print("html", html)

soup = BeautifulSoup(html, 'html.parser')
print('soup', type(soup))
# print in better format.
print('prettify', soup.prettify())

#--------h1----------#
h1 = soup.html.body.h1

# h1 type <class 'bs4.element.Tag'>
print('h1 type',type(h1))
print('h1',h1)
# Now we can get string by using '.string'
print('h1',h1.string)

#--------p----------#
p1 = soup.html.body.p
print("p1", p1)
# Just one is not enough, because it will catch line break(\n).
# To prevent using '.next_sibling' twice, you need to use trim the useless line break and spaces...
p2 = p1.next_sibling.next_sibling
print("p2", p2)

p3 = p1.previous_sibling.previous_sibling
print("p3", p3)

#--------output----------#
print('h1 >> ',h1)
print('p >> ',p1)
print('p >> ',p2)
