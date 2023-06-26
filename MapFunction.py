def addition(n):
    return n+n

##l=[]
##
##for i in range(5):
##    num=int(input("Enter Integer Value : "))
##    data=addition(num)
##    l.append(data)
##
##print(l)

numbers=(12,23,34,45,56)
result=map(addition,numbers)
print(list(result))
