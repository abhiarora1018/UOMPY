from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
j=0
while j<7:
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    i=0
    for tag in tags:
        i=i+1
        if i == 18 :
            url=tag.get('href', None)
            c=tag.string
    j=j+1
print(c)
