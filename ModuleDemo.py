import UDF

while True:
    print("*"*50)
    print("1. OddEven")
    print("2. Maxoftwo")
    print("3. Maxofthree")
    print("4. Prime")
    print("5. Fibonacci")
    print("6. Exit")
    print("*"*50)
    choice=int(input("Enter Your Choice : "))
    print("*"*50)
    if choice==1:
        x=int(input("Enter Value : "))
        UDF.oddeven(x)
        print("*"*50)
    elif choice==2:
        x=int(input("Enter Value : "))
        y=int(input("Enter Value : "))
        UDF.maxoftwo(x,y)
        print("*"*50)
    elif choice==3:
        x=int(input("Enter Value : "))
        y=int(input("Enter Value : "))
        z=int(input("Enter Value : "))
        UDF.maxofthree(x,y,z)
        print("*"*50)
    elif choice==4:
        x=int(input("Enter Value : "))
        UDF.prime(x)
        print("*"*50)
    elif choice==5:
        x=int(input("Enter Value : "))
        UDF.fibonacci(x)
        print("*"*50)
    elif choice==6:
        print("Thank You Using Our Service. Good Bye")
        print("*"*50)
        break
    else:
        print("Invalid Choice.")
        print("*"*50)
