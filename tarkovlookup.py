import requests
word = ('shared bedroom')
x = requests.get('https://tarkov-market.com/api/v1/item?q={}&x-api-key='.format(word))
item = x.json()
item = str(item)
item = (item.split(","))
a,b,c = (item[7], item[10], item[11])
a = a.split(":")
c = c.split(":")
b = b.split(":")
print (a[1])
b =  (b[1])
print (c[1])
b = b.replace("'",'')
print (b)
