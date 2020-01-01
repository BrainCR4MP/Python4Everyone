from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

url = 'http://py4e-data.dr-chuck.net/known_by_Gurdeep.html'
html= urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tags[17].get('href', None))