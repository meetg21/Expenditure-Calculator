users =[]
pocketmoney = []
cost = []
category = []
specificaton = []



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

def add_expense():
    global cost,category,specificaton
    expense.cost = int(input("Enter the cost: "))
    cost.append(expense.cost)
    expense.category = input("Enter the category: ")
    category+=[expense.category,"\n"]
  
    


    expense.specification = input("Enter the specification: ")
    specificaton.append(expense.specification)

    print(str(expense.cost) + " spent")
    print("You have " + str(user.pocketmoney - expense.cost) + " pocketmoney left")
    user.pocketmoney = user.pocketmoney - expense.cost

def show_expense():
    print("Cost")

    for x in cost:
        print(x)
print("Welcome to Machurian , Your Personal Expense Tracker")


print("To add expense press 1 ")
print("To show expenses press 2 ")
print("To add user press 3")

while True:
    t = int(input(">> "))
    if t == 1:
        add_expense()
        
        f = open(user.name+".txt","a+")
        f.writelines(category)
        category.clear()
        
        f.close()
    if t == 2:
        show_expense()
    if t == 3:
        add_user()

    print(category)
    

