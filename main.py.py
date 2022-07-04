

users =[]
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

def add_expense():
    global cost,category,specificaton
    expense.cost = int(input("Enter the cost: "))
    cost.append(expense.cost)
    expense.category = input("Enter the category: ")
    category.append(expense.category)
    expense.specification = input("Enter the specification: ")
    specificaton.append(expense.specification)

    print(str(expense.cost) + " spent")
    print("You have " + str(user.pocketmoney - expense.cost) + " pocketmoney left")

def show_expense():
    print("Cost")

    for x in cost:
        print(x)
print("Welcome to Machurian , Your Personal Expense Tracker")

# print(user.name + "'s account")
print("To add expense press 1 ")
print("To show expenses press 2 ")
print("add user")

while True:
    t = int(input(">> "))
    if t == 1:
        add_expense()
    if t == 2:
        show_expense()
    if t == 3:
        add_user()


