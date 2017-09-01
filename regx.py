import re
f=open('a.txt')
s=0
z=0
l=0
for line in f:
    c=re.findall('[0-9]+',line)
    if len(c)!=0 :
        l=l+len(c)
        z=sum(int(i) for i in c)
        s=s+z
print(s)
