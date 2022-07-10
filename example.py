from tkinter import *
from tkinter import ttk
import json
from tkinter import messagebox
from unicodedata import category, name
from numpy import place
from tkcalendar import DateEntry

def init():
    global data
    try:
        with open("data.json", "r") as f:
            data = json.load(f)
    except:
        data = {"value":[]}
        with open("data.json", "w") as f:
            json.dump(data, f)

def submitexpense():
    values=[dateEntry.get(),Name.get(),Title.get(),Expense.get()]
    if "" not in values:
        print(values)
        data["value"].append(values)
        with open("data.json", "w") as f:
                json.dump(data, f)
        Name.set("")
        Title.set("")
        Expense.set("")
        viewexpense()
    else:
        messagebox.showerror("Error","Invalid value")

def viewexpense():
    root.destroy()
    root2=Tk()
    root2.title("Expense tracker")
    root2.geometry('500x400')
    root2.resizable(False,False)
    pic = PhotoImage(file="icons.png")
    root2.iconphoto(False,pic)
    rows = data["value"]
    amount = 0
    for i in rows:
        amount+=i[3]
    print(rows)
    print(amount)
    
    l=Label(root2,text="Date\t  Name\t  Category\t  Expense",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white")
    l.place(y=50,x=50)

    st=""
    for i in rows:
        for j in i:
            st+=str(j)+'\t'
        st+='\n'
    st+=f"\n \t    \t    \tTotal \t {amount}"
    print(st)
    l=Label(root2,text=st,font=('arial',12))
    l.place(y=100,x=50)

    submitbtn=ttk.Button(root2,command=lambda: [root2.destroy(),mainloop()],text="BACK",width=12)
    submitbtn.grid(row=6,column=0,padx=13,pady=13)



init()
root=Tk()
root.title("Expense tracker")
root.geometry('400x400')
root.resizable(False,False)
pic = PhotoImage(file="icons.png")
root.iconphoto(False,pic)

dateLabel=Label(root,text="Date",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white",width=12)
dateLabel.grid(row=0,column=0,padx=7,pady=7)

dateEntry=DateEntry(root,width=12,font=('arial',15,'bold'))
dateEntry.grid(row=0,column=1,padx=7,pady=7)

Name=StringVar()
nameLabel=Label(root, text="Name",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white",width=12)
nameLabel.grid(row=1,column=0,padx=7,pady=7)

NameEntry=Entry(root,textvariable=Name,font=('arial',15,'bold'))
NameEntry.grid(row=1,column=1,padx=7,pady=7)

Title=StringVar()
titleLabel=Label(root, text="Category",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white",width=12)
titleLabel.grid(row=2,column=0,padx=7,pady=7)

titleEntry=Entry(root,textvariable=Title,font=('arial',15,'bold'))
titleEntry.grid(row=2,column=1,padx=7,pady=7)

Expense=IntVar()
expenseLabel=Label(root,text="Expense",font=('arial',15,'bold'),bg="DodgerBlue2",fg="white",width=12)
expenseLabel.grid(row=3,column=0,padx=7,pady=7)

expenseEntry=Entry(root,textvariable=Expense,font=('arial',15,'bold'))
expenseEntry.grid(row=3,column=1,padx=7,pady=7)

submitbtn=ttk.Button(root,command=submitexpense,text="Submit",width=12 )
submitbtn.grid(row=4,column=0,padx=13,pady=13)


submitbtn=ttk.Button(root,command=viewexpense,text="Expenses",width=12 )
submitbtn.grid(row=6,column=0,padx=13,pady=13)


mainloop()