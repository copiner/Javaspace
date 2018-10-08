import urllib.request

res = urllib.request.urlopen("http://placekitten.com/g/500/600")
kit = res.read()

with open('kit_500_600.jpg','wb') as f:
    f.write(kit)


#object
request = urllib.request.Request("http://placekitten.com/g/400/600")
response = urllib.request.urlopen(request)
cat = response.read()

with open('cat_400_600.jpg','wb') as f:
    f.write(cat)

print(response.geturl())
print(response.info())
print(response.getcode())
