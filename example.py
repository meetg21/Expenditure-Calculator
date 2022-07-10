from tkinter import *
from tkinter import ttk
import json
from tkinter import messagebox
from turtle import back, bgcolor
from unicodedata import category, name
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

def viewexpense():
    global root
    root.destroy()
    root2=Tk()
    root2.title("Display Window")
    root2.geometry('530x500')
    root2.resizable(False,False)
    root2['background']='#CDBA96'
    pic = PhotoImage(file="notes.png")
    root2.iconphoto(False,pic)
    rows = data["value"]
    amount = 0
    for i in rows:
        amount+=i[3]
    print(rows)
    print(amount)
    
    l=Label(root2,text="Date\t        Name\tCategory\t        Expense",font=('roboto',15,'bold','italic'),bg="#8B5A00",fg="white")
    l.place(y=50,x=20)

    st=""
    for i in rows:
        for j in i:
            st+=str(j)+'\t\t'
        st+='\n'
    st+=f"\n\t\t\t                      Total :   ₹{amount}"
    print(st)
    l=Label(root2,text=st,font=('arial',12),background="#CDBA96")
    l.place(y=100,x=20)

    submitbtn=ttk.Button(root2,command=lambda: [root2.destroy(),home()],text="BACK",width=12)
    submitbtn.grid(row=0,column=0,padx=16,pady=300)



init()

def home():
    global root
    root=Tk()
    root.title("Expense Tracker")
    root.geometry('400x270')
    root['background']='#CDBA96'
    root.resizable(False,False)
    pic = PhotoImage(file="stock.png")
    root.iconphoto(False,pic)

    dateLabel=Label(root,text="Date",font=('arial',15,'bold','italic'),bg="#8B5A00",fg="white",width=12)
    dateLabel.grid(row=3,column=0,padx=7,pady=10)

    dateEntry=DateEntry(root,width=12,font=('arial',15,'bold'),bg='#D5B77A')
    dateEntry.grid(row=3,column=1,padx=7,pady=10)

    Name=StringVar()
    nameLabel=Label(root, text="Name",font=('arial',15,'bold','italic'),bg="#8B5A00",fg="white",width=12)
    nameLabel.grid(row=4,column=0,padx=7,pady=10)

    NameEntry=Entry(root,textvariable=Name,font=('arial',15,'bold'),bg='#D5B77A')
    NameEntry.grid(row=4,column=1,padx=7,pady=10)

    Title=StringVar()
    titleLabel=Label(root, text="Category",font=('arial',15,'bold','italic'),bg="#8B5A00",fg="white",width=12)
    titleLabel.grid(row=5,column=0,padx=7,pady=10)

    titleEntry=Entry(root,textvariable=Title,font=('arial',15,'bold'),bg='#D5B77A')
    titleEntry.grid(row=5,column=1,padx=7,pady=10)

    Expense=IntVar()
    expenseLabel=Label(root,text="Expense",font=('arial',15,'bold','italic'),bg="#8B5A00",fg="white",width=12)
    expenseLabel.grid(row=6,column=0,padx=7,pady=10)

    expenseEntry=Entry(root,textvariable=Expense,font=('arial',15,'bold'),bg='#D5B77A')
    expenseEntry.grid(row=6,column=1,padx=7,pady=10)

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

    submitbtn=ttk.Button(root,command=submitexpense,text="Submit",width=12)
    submitbtn.grid(row=7,column=0,padx=13,pady=16)
    # submitbtn.configure(bg="#8B5A00",fg="white")


    submitbtn=ttk.Button(root,command=viewexpense,text="Expenses",width=12 )
    submitbtn.grid(row=7,column=1,padx=13,pady=16)
    mainloop()

home()