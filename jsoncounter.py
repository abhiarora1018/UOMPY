import json
import urllib.request, urllib.parse, urllib.error

url = input('Enter : ')
uh = urllib.request.urlopen(url)
data = uh.read()
info = json.loads(data)
su=0
for item in info["comments"]:
    su=su+(int)(item["count"])
print(su)
