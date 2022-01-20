class bank:
 bal=0
 def __init__(self,accno,name,ac_type,bal):
  self.accno=accno
  self.name=name
  self.ac_type=ac_type
  self.bal=bal

 def display(self):
  print("\nAccount info:")
  print("Account number:",self.accno)
  print("Account name:",self.name)
  print("Account type:",self.ac_type)
  print("Account balance:",self.bal)

 def deposit(self):
  dep=int(input("Enter amount deposit:"))
  self.bal=self.bal+dep

 def withdraw(self):
   w=int(input("Enter amount withdraw:"))
   if w > self.bal:
     print("Insufficient Balance")
   else:
     self.bal=self.bal-w
     print("Rs",w,"Successfully Withdrawn")

acc_no=int(input("Enter Account Number:"))
acc_name=input("Enter name:")
acc_type=input("Enter account type(savings/current):")
balance=int(input("Enter initial balance:"))
b1=bank(acc_no,acc_name,acc_type,balance)

while(1):
 print("\n1.Account info\n2.Deposit\n3.Withdraw\n4.Exit")
 opt=int(input("Select your option:"))
 if opt == 1:
  b1.display()
 elif opt == 2:
  b1.deposit()
 elif opt == 3:
  b1.withdraw()
 elif opt == 4:
  print("Exit")
  break
 else:
  print("Invalid Option")