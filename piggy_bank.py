# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 20:57:50 2018

@author: sidha
"""
#Define class
class PiggyBank:  
    init_amount = 0
#Define functions for class    
    def __init__(self):
        self.interest_rate=.05
    def current_amount(self):
        return PiggyBank.init_amount
    def deposit(self,amount):
        PiggyBank.init_amount = PiggyBank.init_amount + amount
        return PiggyBank.init_amount
    def withdraw(self,amount):
        PiggyBank.init_amount = PiggyBank.init_amount - amount
        return PiggyBank.init_amount
    def calculate_interest(self,months):
        interest=PiggyBank.init_amount*self.interest_rate*months
        principal = PiggyBank.init_amount + interest
        return interest , principal
        


print("-------------------Start-------------------")  
#Create object 
ob1=PiggyBank()

#Input from user
inp_condition = input("Start or End : ") 

#Process application according to user input
while(inp_condition == "Start" or inp_condition == "start" or inp_condition == "START"):
    inp_action=input("Add , Withdraw , Check or Interest : ")
#For Deposit    
    if (inp_action == "Add" or inp_action == "add"):
        inp_amount=float(input("Add Amount : "))
        result=ob1.deposit(inp_amount)
        PiggyBank.init_amount = result
        print("After adding , your updated balance  is {} rupees".format(result))
#For withdrawal        
    elif (inp_action == "Withdraw" or inp_action == "withdraw"):
        inp_amount=float(input("Withdraw Amount : "))
        
        if(inp_amount > PiggyBank.init_amount ):
            print("Insufficient Balance for withdrawal")
        else:            
            result=ob1.withdraw(inp_amount)
            PiggyBank.init_amount = result
            print("After withdrawing ,  balance amount  is {} rupees".format(result))
#To check current balance            
    elif(inp_action == "Check" or inp_action == "check"):
        result=ob1.current_amount()
        print("Your current balance is {} rupees".format(result))
#To calculate interest        
    elif(inp_action == "Interest" or inp_action== "interest"):
        inp_month=float((input("Enter no:of months : ")))
        result_i,result_p = ob1.calculate_interest(inp_month)
        print("Princial is {} and Interest is {} for {} months at 5% interest rate".format(result_p,result_i,inp_month))
    else:
        print("Invalid Option ,  Please enter correct option")
    inp_condition = input("Start or End : ")    
        

        