users =[]
cost = []
category = []
specificaton = []


category_check =[]



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
   
    # pocketmoney.append(user.pocketmoney)
def pocketmoney():
    user.pocketmoney = int(input("Enter your pocketmoney: "))


def add_pocketmoney():
    global cost,category,specification
    addition_pocketmoney = int(input("enter amount u want add in ur pocket money:"))
    user.pocketmoney = user.pocketmoney + addition_pocketmoney
    print(user.pocketmoney)


def add_expense():
    global cost,category,specificaton
    expense.cost = int(input("Enter the cost: "))
    cost.append(expense.cost)


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
    print(p)
    f.close()
    

    expense.specification = input("Enter the specification: ")
    specificaton.append(expense.specification)

    print(str(expense.cost) + " spent")
    user.pocketmoney = user.pocketmoney - expense.cost
    print("You have " + str(user.pocketmoney) + " pocketmoney left")

def show_expense():
    print("Cost")

    for x in cost:
        print(x)
print("Welcome to Expenditure Calculator, Your Personal Expense Tracker")


print("To add expense press 1 ")
print("To show expenses press 2 ")
print("To add user press 3")
print("To add extra money press 4")
print("To add pocketmoney press 5")

while True:
    t = int(input(">> "))
    if t == 1:

        add_expense()
    if t == 2:
        show_expense()
    if t == 3:
        add_user()
    if t == 4 :
        add_pocketmoney()
    if t == 5:
        pocketmoney()

# #%%
# d={}
# username=input("username")
# d["username"]=username
# pocketmoney=int(input(""))
# c+=pocketmoney
# d["pocketmoney"]=c


