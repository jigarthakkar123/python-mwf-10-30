#Function With No Argument & No Return Value.

def printLine():
    print("*"*60)

printLine()
print("Welcome To User Defined Function Using Python.")
printLine()

#Function With Argument But No Return Value.

def add(a,b):
    print("Addition : ",a+b)

printLine()
x=int(input("Enter Value : "))
y=int(input("Enter Value : "))
add(x,y)
printLine()


#Function With Argument & Return Value.

def sub(a,b):
    return a-b

printLine()
x=int(input("Enter Value : "))
y=int(input("Enter Value : "))
ans=sub(x,y)
print("Subtraction : ",ans)
printLine()
