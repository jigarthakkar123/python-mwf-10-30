class Bank:

    def openAccount(self,cname,acno,balance):
        self.cname=cname
        self.acno=acno
        self.balance=balance
        print("Hello ",self.cname+", Your Account Number ",self.acno," Is Opened With ",self.balance," Rs.")
    def deposit(self,amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            self.needs=amount-self.balance
            print("Sorry, You Need Another ",self.needs," Rs. To Withdraw")
    def checkBalance(self):
        print("Your Current Balance : ",self.balance)

b1=Bank()

cname=input("Enter Name Of Customer : ")
acno=int(input("Enter Account Number : "))
balance=int(input("Enter Initial Balance : "))

b1.openAccount(cname,acno,balance)

while True:

    print("*"*60)
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    print("*"*60)

    choice=int(input("Enter Your Choice : "))
    print("*"*60)
    
    if choice==1:
        amount=int(input("Enter Deposit Amount : "))
        b1.deposit(amount)
        print("*"*60)
    elif choice==2:
        amount=int(input("Enter Withdrawal Amount : "))
        b1.withdraw(amount)
        print("*"*60)
    elif choice==3:
        b1.checkBalance()
        print("*"*60)
    elif choice==4:
        print("Thank You Using Our Services. Good Bye")
        print("*"*60)
        break
    else:
        print("Invalid Choice.")
    
