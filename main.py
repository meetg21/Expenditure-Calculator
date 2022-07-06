users =[]
pocketmoney=[]
cost = []
category = []
specificaton = []

x = []
category_check =[]
cost_check = []
specification_check =[]

class user:
    def _init_(self,name,pocketmoney):
        self.name = name
        self.pocketmoney = pocketmoney

class expense:
    def _init_(self,cost,category,specification):
        self.cost = cost
        self.category = category
        self.specification = specification

def add_user():
    user.name = input("Enter your name: ")
    users.append(user.name)
    user.pocketmoney = int(input("Enter your pocketmoney: "))
    pocketmoney.append(user.pocketmoney)

def add_pocketmoney():
    global cost,category,specification
    username = input("Enter your username: ")
    index = users.index(username)
    addition_pocketmoney = int(input("enter amount u want add in ur pocket money:"))
    pocketmoney[index] = pocketmoney[index] + addition_pocketmoney
    # print(user.pocketmoney)


def add_expense():
    global cost,category,specificaton,pocketmoney,users
    username = input("Enter your Username: ")
    index = users.index(username)
    
    expense.cost = int(input("Enter the cost: "))
    expense.cost = str(expense.cost)
    cost+=[expense.cost,"\n"]
    cost_check.append(expense.cost)

    pocketmoney[index] = pocketmoney[index] - int(expense.cost)
    print(users)
    print(pocketmoney)

    a = open(user.name+"cost.txt","a+")
    a.writelines(cost)
    a.close()

    cost.clear()
    a.close()
    a = open(user.name+"cost.txt","r+")
    b = a.read()
    a.close()
    # print(b)
    # print(cost)
############################################
    expense.category = input("Enter the category: ")

    category+=[expense.category,"\n"]
    category_check.append(expense.category)
    # print(category_check)

    f = open(user.name+"category.txt","a+")
    f.writelines(category)
    f.close()
    
    category.clear()
    f.close()
    f = open(user.name+"category.txt","r+")
    p=f.read()
    # print(p)
    # print(category)
    f.close()
    
###########################################3
    expense.specification = input("Enter the specification: ")
    specificaton+=[expense.specification,"\n"]
    specification_check.append(expense.specification)

    v = open(user.name+"specification.txt","a+")
    v.writelines(specificaton)
    v.close()

    specificaton.clear()
    v.close()
    v = open(user.name+"specification.txt","r+")
    w = v.read()
    v.close()
  
    # print(b + w + p) 
    # x.append(b)
    # print(x)




    # print(f(expense.cost + " spent"))
    # user.pocketmoney = user.pocketmoney - int(expense.cost)
    # print(user.pocketmoney)
    print("You have " + str(pocketmoney[index]) + " pocketmoney left")

def display():
    print("Welcome to Expenditure Calculator, Your Personal Expense Tracker")
    print("To add user press 1:")
    print("To set pocketmoney of the user press 2:")
    print("To add expense press 3: ")
    print("To show expenses press 4; ")
    print("To add extra money press 5:")
  
display()
while True:
    
    t = int(input(">> "))
    if t == 1:
        add_user()
    if t == 2:
        pocketmoney()
    if t == 3:
        add_expense()
    if t == 4:
        add_pocketmoney()
       



