# Import tkinter as tk 
import tkinter as tk 
  
  
# creating a new tkinter window 
master = tk.Tk()  
  
# assigning a title 
master.title("HELP-DESK CLASS 5") 
  
# specifying geomtery for window size  
master.geometry("1600x700+0+0") 
lblinfo = tk.Label(master, font=( 'aria' ,30, 'bold' ),text="CBSE HELP DESK FOR CLASS-5",fg="steel blue",bd=10,anchor='w')
lblinfo.place(x=400,y=2)
  
fram=tk.Frame(master,height=250,width=250,bg='yellow')
fram.place(x=10,y=10)


tk.Label(master,font=('aria',20,'bold'),fg='blue', text="Login",width =5,height=1).place(x=70,y=2) 
# label to enter name 
tk.Label(fram,font=('aria',15,'bold'), text="Name :",width = 6,height=1).place(x=5,y=45)
# label for registration number 
tk.Label(fram,font=('aria',15,'bold'), text="Reg.No",width = 6,height=1).place(x=5,y=95)
# label for roll Number 
tk.Label(fram,font=('aria',15,'bold'),text="Roll.No",width = 6,height=1).place(x=5,y=145) 


# declaring objects for entering data 
e1 = tk.Entry(fram) 
e2 = tk.Entry(fram) 
e3 = tk.Entry(fram) 
e1.place(x=100,y=45)
e2.place(x=100,y=95)
e3.place(x=100,y=145)





def action():
    fram1=tk.Frame(master,height=300,width=1000,bg='cyan')
    fram1.place(x=300,y=150)
    tk.Label(fram1,font=('aria',22),fg='red', text="Hello " + e1.get() +" please Enter Below which problem's Solution you Want :",width =60,height=1).place(x=0,y=45) 
    e4 = tk.Entry(fram1)
    e5 = tk.Entry(fram1)
    e4.place(x=450,y=130)  
    e5.place(x=450,y=160)
    tk.Label(fram1,font=(500), text="Enter Subject Name:",width =15,height=1).place(x=300,y=130) 
    tk.Label(fram1,font=(500), text="Enter Chapter No. :",width =15,height=1).place(x=300,y=160)
    search_but=tk.Button(fram1,font=('aria',15),text="Search",fg='red')
    search_but.place(x=410,y=200)




  
submit_but=tk.Button(master,font=('aria',15),text="submit",command=action,fg='red')
submit_but.place(x=80,y=190)

      
master.mainloop() 
   
   
   