from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_conn():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python_10_30_mwf"
        )

def insert_data():
    if e_ename.get()=="" or e_dept.get()=="" or e_salary.get()=="":
        msg.showinfo("Insert Status","All Fields Are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="insert into emp(ename,dept,salary) values(%s,%s,%s)"
        args=(e_ename.get(),e_dept.get(),e_salary.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_ename.delete(0,"end")
        e_dept.delete(0,"end")
        e_salary.delete(0,"end")
        msg.showinfo("Insert Status","Insert Data Sucessfully")

def search_data():
    e_ename.delete(0,"end")
    e_dept.delete(0,"end")
    e_salary.delete(0,"end")
    if e_id.get()=="":
        msg.showinfo("Search Status","Id Is Mandatory For Search")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="select * from emp where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        if row:
            for i in row:
                e_ename.insert(0,i[1])
                e_dept.insert(0,i[2])
                e_salary.insert(0,i[3])
        else:
            msg.showinfo("Search Status","Id Not Found")
        conn.close()

def update_data():
    if e_ename.get()=="" or e_dept.get()=="" or e_salary.get()=="" or e_id.get()=="":
        msg.showinfo("Update Status","All Fields Are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="update emp set ename=%s,dept=%s,salary=%s where id=%s"
        args=(e_ename.get(),e_dept.get(),e_salary.get(),e_id.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_ename.delete(0,'end')
        e_dept.delete(0,'end')
        e_salary.delete(0,'end')
        e_id.delete(0,'end')
        msg.showinfo("Update Status","Data Updated Successfully")

def delete_data():
    if e_id.get()=="":
        msg.showinfo("Delete Status","Id Is Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="delete from emp where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_ename.delete(0,'end')
        e_dept.delete(0,'end')
        e_salary.delete(0,'end')
        e_id.delete(0,'end')
        msg.showinfo("Delete Status","Data Deleted Successfully")

root=Tk()
root.geometry("330x390")
root.title("My Desktop Application")
root.resizable(width=False,height=False)

l_id=Label(root,text="ID",font=("Algerian",15))
l_id.place(x=50,y=50)

l_ename=Label(root,text="ENAME",font=("Algerian",15))
l_ename.place(x=50,y=100)

l_dept=Label(root,text="DEPT",font=("Algerian",15))
l_dept.place(x=50,y=150)

l_salary=Label(root,text="SALARY",font=("Algerian",15))
l_salary.place(x=50,y=200)

e_id=Entry(root)
e_id.place(x=150,y=50)

e_ename=Entry(root)
e_ename.place(x=150,y=100)

e_dept=Entry(root)
e_dept.place(x=150,y=150)

e_salary=Entry(root)
e_salary.place(x=150,y=200)

insert=Button(root,text="INSERT",font=("Algerian",15),bg="black",fg="white",command=insert_data)
insert.place(x=50,y=250)

search=Button(root,text="SEARCH",font=("Algerian",15),bg="black",fg="white",command=search_data)
search.place(x=180,y=250)

update=Button(root,text="UPDATE",font=("Algerian",15),bg="black",fg="white",command=update_data)
update.place(x=50,y=300)

delete=Button(root,text="DELETE",font=("Algerian",15),bg="black",fg="white",command=delete_data)
delete.place(x=180,y=300)

root.mainloop()
