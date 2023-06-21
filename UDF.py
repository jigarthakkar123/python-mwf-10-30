def oddeven(a):
    if a % 2== 0:
        print(a,"is even number")
    else:
        print(a,"is odd number")

def maxoftwo(a,b):
    if a>b:
        print(a," is greater")
    else :
        print(b," is greater")

def maxofthree(a,b,c):
    if a>b:
        if a>c:
            print(a," is greater")
        else:
            print(c," is greater")
    elif b>c:
        print(b," is grater")
    else:
        print(c," is greater")

def prime(n):
    if n%2!= 0:
        for i in range (3,int(n/2)+1,2):
            if n%i == 0:
                print(n," not prime num")
                break
        else:
            print(n," is prime")
    else:
        print(n," is not prime")

def fibonacci(n):
    a,b=0,1
    print(a,end=" ")
    while b<n:
        print(b,end=" ")
        a,b=b,a+b
    print()
