
class BankAcount:
    def __init__(self,name):
        
        self.name = name
        self.balance = balance = 0

    def deposit(self, amount):
        self.amount = amount

        if amount<=0:
            print("Negative Amount can not be Deposit")
        else:
            self.balance+=amount
            print(f"{self.name} deposit {self.amount}")
    
    def Withdraw(self, amount):
        self.amount = amount
        if amount>self.balance:
            print("Not enought balance")
        else:
            self.balance-=amount
            print(f"{self.name} Withdraw {self.amount}. Your Remaining Balance is {self.balance}")
    
    def view(self):
        print(f"Your total amount is{self.balance}")

class SavingAcount(BankAcount):
    def addInterest(self):
        interest = self.balance*0.05
        self.balance+=interest
        print(f"{self.name}amount with added interest is {self.balance}")

# username = input("Enter Your Name :")
# n = SavingAcount(username)
# deposit = int(input ("Enter the amount you want to deposit"))
# n.deposit(deposit)
# withdraw = int(input ("Enter the amount you want to withdraw"))
# n.Withdraw(withdraw)
# n.view()
# n.addInterest()
username = input("Enter Your Name :")
n = SavingAcount(username)

while True:
    print("\n--- Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. View Balance")
    print("4. Add Interest")
    print("5. Exit")

    choice = int(input("Enter your choice (1-5): "))
    
    if choice == 1:
        amount = int(input("Enter amount to deposit: "))
        n.deposit(amount)
    elif choice == 2:
        amount = int(input("Enter amount to withdraw: "))
        n.Withdraw(amount)
    elif choice == 3:
        n.view()
    elif choice ==4:
        n.addInterest()
    elif choice==5:
        break
    else:
            print("Invalid choice. Please enter a number between 1 and 3.")

# deposit = int(input ("Enter the amount you want to deposit"))
# n.deposit(deposit)
# withdraw = int(input ("Enter the amount you want to withdraw"))
# n.Withdraw(withdraw)
# n.view()
# n.addInterest()

# elif choice == "2":
#         amount = int(input("Enter amount to withdraw: "))
#         account.withdraw(amount)
# elif choice == "3":
#         account.view()
#          break
#      else:
#             print("❌ Invalid choice. Please enter a number between 1 and 3.")
