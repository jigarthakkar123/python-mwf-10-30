#from collections import Counter

d1={"A":1,"B":2,"C":3,"D":4}
d2={"A":5,"C":10,"D":15,"E":10}
d3={}

#d3=Counter(d1)+Counter(d2)
#print(d3)
for i in d1:
    if i in d2:
        d3[i]=d1[i]+d2[i]
    else:
        d3[i]=d1[i]
    for j in d2:
        if j not in d3:
            d3[j]=d2[j]
print(d3)
