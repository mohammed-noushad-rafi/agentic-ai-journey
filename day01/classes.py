# Write a class BankAccount with a balance attribute that starts at 0. Give it deposit(amount) and withdraw(amount) methods. withdraw should return "Insufficient funds" if the amount is more than the balance

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

# Write a dataclass Task with 
# title: str and done: bool = False. Create 2 tasks and print them.
from dataclasses import dataclass 
@dataclass 
class Task:
    title:str
    done:bool=False

updates=Task("python3block",True)
task2=Task("Learn Big-O",)
print(updates)
print(task2)
print(updates.title)    


# Make a list of 3 Message dataclass objects and 
# print only the content of the ones where role == "user".
from dataclasses import dataclass
@dataclass
class messages:
    content:str
    role:str

messages = [messages("hello","admin"),
          messages("hi","security"),
          messages("hello","user"),]
for message in messages :
    if message.role=="user":
        print(message.content)