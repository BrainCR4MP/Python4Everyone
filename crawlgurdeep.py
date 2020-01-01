from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error

# iteration variable for while loop
sum = 0

url = 'http://py4e-data.dr-chuck.net/known_by_Gurdeep.html'

# loop for opening url, take 18th(17) link and store it to url.
while sum < 7:
    # open url and parse html
    html= urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    # make a list of links
    tags = soup('a')

    # store 18th link in "tags" list
    x = tags[17].get('href', None)

    #change url to be opened again
    url = x

    # iteration variable and print
    sum = sum +1
    print(x)

