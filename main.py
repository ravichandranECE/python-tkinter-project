

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import database

db=database("employees.db")
root=Tk()
root.title("college  management")
root.geometry("1280x720+0+0")
root.config(bg="gray")

name=StringVar()
age=StringVar()
dept=StringVar()
clg=StringVar()

entries_frame=Frame(root,bg="black")
entries_frame.pack(
    side=TOP,fill=X)
title=Label(entries_frame,text="college management",font=("calibri",18,"bold"), bg="black", fg="white")
title.grid(row=0,columnspan=2)

lblName=Label(entries_frame,text="NAME",font=("calibri",13), bg="black",fg="white")
lblName.grid(row=1,column=0,sticky=W,pady=30)
txtName=Entry(entries_frame,textvariable=name,width=25)

txtName.grid(row=1,column=1,padx=10,sticky=W,pady=30)


lblAge=Label(entries_frame,text="AGE",font=("calibri",13), bg="black",fg="white")
lblAge.grid(row=1,column=2,sticky=W)
txtAge=Entry(entries_frame,textvariable=age,width=25)
txtAge.grid(row=1,column=3,padx=10,sticky=W)

lbldept=Label(entries_frame,text="DEPT",font=("calibri",13), bg="black",fg="white")
lbldept.grid(row=2,column=0,pady=15,sticky=W)
combodept = ttk.Combobox(entries_frame, font=("calibri",13), width=15, textvariable=dept, state="readonly")

combodept["values"] = ("ECE","CSE","EEE","IT","TC","TT","MECH","PCT","CIVIL")
combodept.grid(row=2,column=1,padx=10,sticky=W,pady=10)

lblClg=Label(entries_frame,text="CLG",font=("calibri",13), bg="black",fg="white")
lblClg.grid(row=2,column=2,sticky=W,pady=10)
txtClg=Entry(entries_frame,textvariable=clg,width=25)
txtClg.grid(row=2,column=3,padx=10,sticky=W,pady=10)

def getdata(event):
    select_row = tv.focus()
    data = tv.item(select_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1])
    age.set(row[2])
    dept.set(row[3])
    clg.set(row[4])



def displayall():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)


def add_student():
    if txtName.get()=="" or txtAge.get()=="" or combodept.get()=="" or txtClg.get()=="":
        messagebox.showerror("error in input","please fill the all details")

        return
    db.insert(txtName.get(),txtAge.get(),combodept.get(),txtClg.get())
    messagebox.showerror("sucess","record inserted")
    clearall()
    displayall()

def update_student():
    if txtName.get() == "" or txtAge.get() == "" or combodept.get() == "" or txtClg.get() == "":
        messagebox.showerror("error in input", "please fill the all details")
        return
    db.update(row[0], txtName.get(), txtAge.get(), combodept.get(), txtClg.get())
    messagebox.showerror("sucess", "record updated")
    clearall()
    displayall()



def delete_student():
    db.remove(row[0])
    clearall()
    displayall()
def clearall():
    name.set("")
    age.set("")
    dept.set("")
    clg.set("")


btn_frame=Frame(entries_frame,bg="black")
btn_frame.grid(row=4,column=0,padx=5,pady=30,sticky=W)

btnAdd=Button(btn_frame,command=add_student,text="add details",bg="red",fg="black",border=5).grid(row=5,column=0)

btn_frame=Frame(entries_frame,bg="black")
btn_frame.grid(row=4,column=1,padx=5,pady=30,sticky=W)
btndelete=Button(btn_frame,command=delete_student,text="delete detail",bg="blue",fg="black",border=5).grid(row=5,column=1)

btn_frame=Frame(entries_frame,bg="black")
btn_frame.grid(row=4,column=2,padx=5,pady=30,sticky=W)
btnclear=Button(btn_frame,command=clearall,text="clear all",bg="green",fg="black",border=5).grid(row=5,column=2)


btn_frame=Frame(entries_frame,bg="black")
btn_frame.grid(row=4,column=3,padx=5,pady=30,sticky=W)
btnclear=Button(btn_frame,command=update_student,text="update",bg="yellow",fg="black",border=5).grid(row=5,column=2,padx=20)




tree_frame = Frame(root,bg="white")
tree_frame.place(x=0, y=300, width=1288,height=666)
style = ttk.Style()
style.configure("mystyle.Treeview",font=("calibri",15),
                rowheight=50)#,modify the font of the body
style.configure("mystyle.Treeviews.heading",font=("calibri",30,"Bold"))#modify the font of the headings

tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,),style="mystyle.Treeview")
tv.heading("1", text="id")
tv.column("1",width=5)
tv.heading("2", text="name")
tv.heading("3", text="age")
tv.column("3",width=5)
tv.heading("4", text="dept")
tv.column("4",width=5)
tv.heading("5", text="clg")
tv["show"] = "headings"
tv.bind("<ButtonRelease-1>", getdata)
tv.pack(fill=X)

displayall()
displayall()
root.mainloop()

