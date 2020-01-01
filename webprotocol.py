import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

#Command to GET and send command
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

#check if there is data
while True:
    data = mysock.recv(512)
    #if no data, then break
    if (len(data) < 1):
        break
    #if there is data, encode it to user
    print(data.decode())
#remember to close connection/socket
mysock.close()


# # Minibrowser, webcrawler
# # Or do it like this boiiiii
import urllib.request, urllib.parse, urllib.error
# # create handle
fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# # go through lines, decode, strip and print for user.
for line in fhand:
     print(line.decode().strip())

# # You can continue code by searching href= links in lines.
# # update urllib.request.urlopen(new url here) with found links, and you have göögle.

