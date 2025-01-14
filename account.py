
class Account:
    def __init__(self,accno,name,typ,bal):
        self.accno=accno
        self.name=name
        self.typ=typ
        self.bal=bal
    def deposit(self,amt):
        if amt<0:
            print('Enter a valid amount')
        else:
            self.bal+=amt
            print(amt," sucessfully Deposited")
            print("current balance = ",self.bal)
    def withdraw(self,amt):
        if amt>self.bal:
            print("insufficient balance")
        elif amt < 0:
            print('Enter a valid amount')
        else:
            self.bal-=amt
            print(amt," sucessfully withdrawn")
            print("current balance = ",self.bal)
    def balance(self):
        print("current balance = ",self.bal)
    def display(self):
        print("Account Details")
        print("account no :",self.accno)
        print("account holder name :",self.name)
        print("account type :",self.typ)
        print("account balance :",self.bal)
        
        
accno=int(input("acc no"))
name=input("name")
typ=input("type")
bal=int(input("balance"))
account=Account(accno,name,typ,bal)

flag=True

while flag:
    print("\n Menu")
    print("1. Deposit ")
    print("2. Withdraw ")
    print("3. Current Balance")
    print("4. View Details")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        amt = int(input("Enter amount to be deposited: "))
        account.deposit(amt)
    elif choice == 2:
        amt = int(input("Enter amount to withdraw: "))
        account.withdraw(amt)
    elif choice == 3:
        account.balance()
    elif choice == 4:
        account.display()
    elif choice == 5:
        print("Exited")
        flag = False
    else:
        print("Invalid choice, please try again.")

