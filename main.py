
import tkinter as tk
from PIL import Image,ImageTk 
import random as rn
import pymysql as pym
import datetime as dt
 
i=5
x=0
s=0
checkbox_var=[]
lister=[]
date_now=dt.date.today()
    #database
db=pym.connect(host="localhost",user="root",passwd="",database="to_do")
cur=db.cursor() 
def room():
    global todo,root
    root=tk.Tk()
    todo=tk.StringVar()
    root.geometry("450x600")
    root.iconbitmap(r"Todolist/assets/tick.ico") #for relative path
    root.title("To Do Rabbit")
    root.configure(background="black",padx=20,pady=20)      
    new()

    


    



def submit():
    global db
    roto=todo.get()
    sql="insert into tbl_tasks(task_name,status,date) values (%s,%s,%s)"
    val=(roto,0,date_now)
    cur.execute(sql,val)
    db.commit()
    cc=tk.Label(root,text="Inserted Successfully !!", font=('calibre',10, 'bold'),bg="black",fg="#DE4D86")
    cc.grid(row=1,column=1)
    
def add(index,x):
    global checkbox_var,db
    if checkbox_var[index].get() == 1:
        up="update tbl_tasks set status=%s where task_name=%s"
        val=(1,x)
        cur.execute(up,val)
        db.commit()
    
def view_done():
    sel="select task_name from tbl_tasks where date=%s and status=%s"
    val=(date_now,1)
    cur.execute(sel,val)
    result=cur.fetchall()
    global i,root
    for x in result:                
        c1 = tk.Label(root, text=x,font=('calibri',12,'bold'),bg="black",foreground="#FCDE70")    
        c1.grid(row=i,column=1)
        i+=1
        
def view_it():
    sele="select task_name from tbl_tasks where date=%s and status=%s"
    val=(date_now,0)
    cur.execute(sele,val)
    result=cur.fetchall()
    global i
    global checkbox_var
    s=0
    for x in result:
        var = tk.IntVar()
        checkbox_var.append(var)                
        c1 = tk.Checkbutton(root, text=x[0],variable=var,onvalue=1,offvalue=0,font=('calibri',12,'bold'),bg="black",foreground="#DE4D86")    
        var.trace_add("write", lambda *args, index=s,text=x[0]:add(index,text))
        s+=1
        c1.grid(row=i,column=1)
        i+=1 
    #view_done()
   
def delet():
    global root,db
    mn="delete from tbl_tasks"
    cur.execute(mn)
    db.commit()
    i=10
    x=str(cur.rowcount)+" record(s) deleted !!,\nyou will not see todays \nentries after refreshing."
    msg=tk.Label(root,text=x,font=('calibre',10, 'bold'),bg="black",fg="#DE4D86")
    msg.grid(row=20,column=1)
    
def delet_s1():
    global root,db
    mn="delete from tbl_tasks where status=1"
    cur.execute(mn)
    db.commit()
    x=str(cur.rowcount)+" record(s) deleted !!,\nRefresh,please"
    msg=tk.Label(root,text=x,font=('calibre',10, 'bold'),bg="black",fg="#DE4D86")
    msg.grid(row=20,column=1)
    
def refresh():
    root.destroy()
    global i
    i=5
    room()
        
def new():
    todos = tk.Label(root, text = 'New entry:', font=('calibre',10, 'bold'),bg="black",fg="white")
    spaces = tk.Label(root, text = '\n',bg="black")
    todoentry = tk.Entry(root,textvariable = todo ,justify="center",font=('calibre',10,'normal'))
    todoentry.delete(0,tk.END)
    sub=tk.Button(root,text = 'Submit',bg="#DE4D86",fg="#64113F",command=submit)
    dele=tk.Button(root,text = '   Delete All  ',bg="#DE4D86",fg="#64113F",command=delet)
    dele_s1=tk.Button(root,text = 'Delete Done',bg="#DE4D86",fg="#64113F",command=delet_s1)
    view=tk.Button(root,text = '  View to do',bg="#DE4D86",fg="#64113F",command=view_it)
    viewt=tk.Button(root,text = ' Tasks Done',bg="#DE4D86",fg="#64113F",command=view_done)
    ref=tk.Button(root,text = '     Refresh   ',bg="#DE4D86",fg="#64113F",command=refresh)


        #positions
    todos.grid(row=0,column=0)
    todoentry.grid(row=0,column=1)
    sub.grid(row=0,column=2)
    spaces.grid(row=1,column=0)
    viewt.grid(row=5,column=0)
   
    view.grid(row=6,column=0)
    
    ref.grid(row=7,column=0)
    
    dele_s1.grid(row=8,column=0)

    dele.grid(row=10,column=0)    
    
    #images
    images= [Image.open(r"Todolist/assets/dancing-smiling.gif"),
                Image.open(r"Todolist/assets/dance-dancing.gif"),
                Image.open(r"Todolist/assets/dancrabi.gif"),
                Image.open(r"Todolist/assets/eminem.gif"),
                Image.open(r"Todolist/assets/blued.gif"),
                Image.open(r"Todolist/assets/buny.gif"),
                Image.open(r"Todolist/assets/new.gif")]
    new=rn.choice(images)
    photo = ImageTk.PhotoImage(new)
    label = tk.Label(root, image=photo,bg="black")
    label.grid(row=14,column=2,padx=5,pady=10)
    root.mainloop()
   
        
room()
#loop
