import urllib.parse,urllib.error
from urllib.request import urlopen

fhand=urlopen('http://data.pr4e.org/cover3.jpg')
counts=dict()
for line in fhand:
    words=line.decode().split()
    for word in words:
        counts[word]=2
        print(counts)