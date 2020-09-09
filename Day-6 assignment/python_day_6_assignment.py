# -*- coding: utf-8 -*-
"""Python day-6 assignment

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1w7-EEYBOcANXkWUS8uM2An99xEo4Y3ik

##For this challenge,create a bank account class that has two attributes
*ownerName
*Balance
And two methods
*deposit
*withdraw
As an added requirement,withdrawals may not exceed the available balance.
Instantiate your class,make several deposits and withdrawals,and test to make sure the account
cant be overdrawn.
"""

class bankaccount():
    def __init__(self,ownername,balance):
        self.ownername=ownername
        self.balance=balance
 
    def deposit(self,amount):
        self.balance=self.balance+amount
        print("Amount deposited = ",amount)
        print("Total avaialable balance = ",self.balance)
 
    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance=self.balance-amount
            print("Amount withdrawn = ",amount)
            print("Total avaialable balance = ",self.balance)
        else:
            print("Total avaialable balance = ",self.balance)
            print("You can't withdraw morethan your avaialable balance")
 
#operations
customer1 = bankaccount ("kumar",0)
response="blank"
while response !="D" or response !="W":
    response=input("Enter D to depost or W to withdraw C to cancel the operation")
    if response == "D":
# depositing money
        customer1.deposit(int(input("enter amount to deposit = ")))
       
    elif response == "W":
# withdrawing money
        customer1.withdraw(int(input("enter amount to withdraw = ")))
    elif response == "C":
        break

"""##For this challenge,create a cone class that has two attributes:
*R=Radius
*h=Height
And two methods:
*Volume = Π * r2 = (h/3)
*Surface area : base : Π * r2 , side : Π * r * √(r2 + h2)
Make only one class with functions,as in where required import Math.
"""

import math
class cone():
    def __init__(self,radius,height):
        self.r=radius
        self.h=height
 
    def volume(self):
        Volume=1/3 * math.pi * self.r**2 * self.h
        print("Volume of cone is {}cm\u00b3".format(Volume))
    def surfacearea(self):
        base = math.pi * self.r**2
        side = math.pi * self.r * (math.sqrt(self.r**2 +self.h**2))
        Surfacearea = base + side
        print("Surfacearea of cone is {}cm\u00b2".format(Surfacearea))
 
#operations
h = int(input("enter height of the cone in cm = "))
r = int(input ("enter radius of the cone in cm = "))
obj1 = cone(h,r)
obj1.volume()
obj1.surfacearea()
