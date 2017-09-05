import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter : ')
uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)
results = tree.findall('.//count')
su=0
for tag in results:
    su=su+(int)(tag.text)
print(su)

