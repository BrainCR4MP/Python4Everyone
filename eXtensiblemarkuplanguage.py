import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error

sum = 0
url = 'http://py4e-data.dr-chuck.net/comments_311437.xml'
html = urllib.request.urlopen(url).read()
tree = ET.fromstring(html)
list = tree.findall('comments/comment')
for item in list:
    num = item.find('count').text
    x = int(num)
    sum = sum + x
print(sum)