#making web sockets easy using library urllib.
#since HTTP is so common, we use this library that makes web pages look like a file

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in fhand:
    print(line.decode().strip())
    
#no headers here


    
    
    
