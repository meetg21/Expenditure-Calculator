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


    a = open(users[index]+"cost.txt","a+")
    a.writelines(cost)
    a.close()

    cost.clear()
    a.close()
    a = open(users[index]+"cost.txt","r+")
    b = a.read()
    a.close()
    # print(b)
    # print(cost)
############################################
    expense.category = input("Enter the category: ")

    category+=[expense.category,"\n"]
    category_check.append(expense.category)
    # print(category_check)

    f = open(users[index]+"category.txt","a+")
    f.writelines(category)
    f.close()
    
    category.clear()
    f.close()
    f = open(users[index]+"category.txt","r+")
    p=f.read()
    # print(p)
    # print(category)
    f.close()
    
###########################################3
    expense.specification = input("Enter the specification: ")
    specificaton+=[expense.specification,"\n"]
    specification_check.append(expense.specification)

    v = open(users[index]+"specification.txt","a+")
    v.writelines(specificaton)
    v.close()

    specificaton.clear()
    v.close()
    v = open(users[index]+"specification.txt","r+")
    w = v.read()
    v.close()
    print(users[index])
    # print(b + w + p) 
    # x.append(b)
    # print(x)



def show_expense():
   global cost,category,specificaton,pocketmoney,user
   username = input("Enter your Username: ")
   index = users.index(username)
   print("You have " + str(pocketmoney[index]) + " pocketmoney left") 

def display():
    print("Welcome to Expenditure Calculator, Your Personal Expense Tracker")
    print("To add user press 1:")
    print("To add expense press 2: ")
    print("To show expenses press 3; ")
    print("To add extra money press 4:")
  
display()
while True:
    
    t = int(input(">> "))
    if t == 1:
        add_user()
    if t == 2:
        add_expense()
    if t == 3:
       show_expense()
    if t == 4:
        add_pocketmoney()
       



