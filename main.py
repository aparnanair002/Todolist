
import tkinter as tk
from PIL import Image,ImageTk 
import random as rn
import pymysql as pym
import datetime as dt
  
root=tk.Tk()

root.geometry("450x600")
root.iconbitmap(r"assets/tick.ico") #for relative path
root.title("To Do Rabbit")
root.configure(background="black",padx=20,pady=20)

todo=tk.StringVar()
i=10
x=0
lister=[]
date_now=dt.date.today()
#database
db=pym.connect(host="localhost",user="root",passwd="",database="to_do")
cur=db.cursor()



def submit():
    roto=todo.get()
    sql="insert into tbl_tasks(task_name,status,date) values (%s,%s,%s)"
    val=(roto,0,date_now)
    cur.execute(sql,val)
    db.commit()
    cc=tk.Label(root,text="Inserted Successfully !!", font=('calibre',10, 'bold'),bg="black",fg="#DE4D86")
    cc.grid(row=1,column=1)

def view_it():
    sele="select task_name from tbl_tasks where date=%s"
    val=date_now
    cur.execute(sele,val)
    result=cur.fetchall()
    global i
    for x in result:        
        cc=tk.Label(root,text=x, font=('calibre',10, 'bold'),bg="black",fg="#DE4D86")
        c1 = tk.Checkbutton(root, text=x,onvalue=1, offvalue=0,font=('calibri',12,'bold'),bg="black",foreground="#DE4D86")
        cc.grid(row=i,column=1)
    i+=1
   
def delet():
    mn="delete from tbl_tasks"
    cur.execute(mn)
    db.commit()
    x=str(cur.rowcount)+" record(s) deleted !!,\nyou will not see todays \nentries after refreshing."
    msg=tk.Label(root,text=x,font=('calibre',10, 'bold'),bg="black",fg="#DE4D86")
    msg.grid(row=4,column=1)
    
def refresh():
    root.update()
    root.update_idletasks()


        
      
#labels
todos = tk.Label(root, text = 'New entry:', font=('calibre',10, 'bold'),bg="black",fg="white")
spaces = tk.Label(root, text = '\n',bg="black")
todoentry = tk.Entry(root,textvariable = todo ,justify="center",font=('calibre',10,'normal'))
todoentry.delete(0,tk.END)
sub=tk.Button(root,text = 'Submit',bg="#DE4D86",fg="#64113F",command=submit)
ref=tk.Button(root,text = 'Refresh',bg="#DE4D86",fg="#64113F",command=refresh)
dele=tk.Button(root,text = 'Delete All Entries',bg="#DE4D86",fg="#64113F",command=delet)
view=tk.Button(root,text = 'View All Entries',bg="#DE4D86",fg="#64113F",command=view_it)




#positions
todos.grid(row=0,column=0)
todoentry.grid(row=0,column=1)
sub.grid(row=0,column=2)
ref.grid(row=0,column=3)
spaces.grid(row=2,column=0)
dele.grid(row=2,column=1)
view.grid(row=3,column=1)

spaces.grid(row=6,column=1)



#images

image = [Image.open(r"assets/dancing-smiling.gif"),
         Image.open(r"assets/dance-dancing.gif"),
         Image.open(r"assets/dancrabi.gif"),
         Image.open(r"assets/eminem.gif"),
         Image.open(r"assets/blued.gif"),
         Image.open(r"assets/buny.gif"),
         Image.open(r"assets/new.gif")]
new=rn.choice(image)
photo = ImageTk.PhotoImage(new)
label = tk.Label(root, image=photo,bg="black")
label.grid(row=14,column=2,padx=5,pady=10)

#loop
root.mainloop()