s=input("Enter String : ")

upper=0
lower=0
char=0
digit=0
space=0

for i in s:
    if i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    if i.isalpha():
        char+=1
    elif i.isnumeric():
        digit+=1
    elif i.isspace():
        space+=1

print("Total Upper : ",upper)
print("Total Lower : ",lower)
print("Total Char : ",char)
print("Total Digit : ",digit)
print("Total Space : ",space)
