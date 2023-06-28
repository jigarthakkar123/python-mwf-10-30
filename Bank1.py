class Bank:

    def openAccount(self,cname,acno,balance,actype):
        self.cname=cname
        self.acno=acno
        self.balance=balance
        self.actype=actype
        #print("Hello ",self.cname+", Your Account Number ",self.acno," Is Opened With ",self.balance," Rs.")
    
    def display(self):
        print("Account Holder name is: ",self.cname)
        print("Account number is: ",self.acno)
        print("balace is: ",self.balance)
        print("account type is: ",self.actype)
        
b1=Bank()

cname=input("Enter Name Of Customer : ")
acno=int(input("Enter Account Number : "))
balance=int(input("Enter Initial Balance : "))
print("Select account type")
print("1.Saving")
print("2.Current")
print("3.NRI")
t1=int(input("enter choice: "))

if t1==1:
    actype="Saving"
elif t1==2:
    actype="Current"
elif t1==3:
    actype="NRI"
else:
    print("Invalid Choice")

b1.openAccount(cname,acno,balance,actype)
b1.display()
