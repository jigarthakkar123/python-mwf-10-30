t=(1,2,1.1,2.2,"tops",[100,200,300],True,10,20,"Python")

print(t)
print(t.count(1))
print(t.index(10))
for i in t:
    print(i)
print(10 in t)
print(t[5])
t[5].append(400)
print(t)
