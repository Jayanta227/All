import json
adbook={}
adbook["Jay"]={
    'name':'jayanta',
    'phone':'264687'}
adbook["ujjal"]={
    'name':'u Ghosh',
    'phone':'2646487'}
s=json.dumps(adbook)
with open("jsn.txt","r+") as f:
    f.write(s)
with open("jsn.txt","r+") as f:
    book=json.loads(f.read())
print(book)
