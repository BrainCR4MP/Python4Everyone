#

from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

sum = 0
url = 'http://py4e-data.dr-chuck.net/comments_311435.html'
html= urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('span')
for tag in tags:
    x = int(tag.contents[0])
    sum += x
print(sum)