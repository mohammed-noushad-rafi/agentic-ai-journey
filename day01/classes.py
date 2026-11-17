class BankAccount:
    def __init__(self,balance=0):
        self.balance=balance
        pass
    def deposit(self,amount):
       self.amount=amount
       if amount >0:
          self.balance+=amount
          print("added to account")
          return self.balance 
    def withdraw(self,amount):
        if amount > self.balance:
         return "Insufficient funds"
        else :
          self.balance -=amount
        return self.balance
SBI=BankAccount(10000)
print(SBI.withdraw(123))
account = BankAccount()
account.deposit(500)
print(account.balance)
print(account.withdraw(200))
print(account.withdraw(1000))
print(account.balance)

        