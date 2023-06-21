d={231:"Vishal",765:"Bhargav",908:"Rinkal",564:"Krina",434:"Krishna"}

print(d)
print(d[765])
#print(d["Krina"])
print(d.get(908))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(564))
print(d)
print(d.popitem())
d1={101:"Krina",102:"Krishna",103:"Anchal",105:"Sohan"}
d.update(d1)
print(d)

for i in d:
    print(i," : ",d[i])
