from distutils.cmd import Command
from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
from tkcalendar import DateEntry

class Student:
    
    def __init__(self,root):
        self.root = root
        self.root.title("Sanjivani College of Engineering (Yellow Book)")
        self.root.geometry("1350x200")
        
        title = Label(self.root,text="Laboratory Register",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="black",fg="yellow")
        title.pack(side=TOP,fill=X)
        
        # ALL VARIABLES ===>
        self.Sr_No_var = StringVar()
        self.Exp_No_var = StringVar()
        self.Batch_var = StringVar()
        self.Roll_No_var = StringVar()
        self.DoSE_var = StringVar()
        self.DoCE_var = StringVar()
        self.EDEC_var = StringVar()
        self.DEC_var = StringVar()
        self.Marks_var = StringVar()
        
        self.search_by = StringVar()
        self.search_txt = StringVar()

        
        # MANAGE FRAME ===>
         
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="yellow")
        Manage_Frame.place(x=10,y=90,width=450,height=650)
        
        m_title = Label(Manage_Frame,text="Enter Lab Record",fg="black",bg="yellow",font=("times new roman", 20, "bold"))
        m_title.grid(row=0,columnspan=2,pady=20)
        
        # Sr No
        srnol = Label(Manage_Frame,text="Sr No",fg="black",bg="yellow",font=("times new roman", 15))
        srnol.grid(row=1,column=0,pady=17,padx=17,sticky="w")
        
        txt_srno = Entry(Manage_Frame,textvariable=self.Sr_No_var,font=("times new roman", 10),bd=5,relief=GROOVE)
        txt_srno.grid(row=1,column=1,pady=17,padx=17,sticky="w")
        
        # Exp No.
        lbl_expno = Label(Manage_Frame,text="Exp No",fg="black",bg="yellow",font=("times new roman", 15))
        lbl_expno.grid(row=2,column=0,pady=17,padx=17,sticky="w")
        
        txt_expno = Entry(Manage_Frame,textvariable=self.Exp_No_var,font=("times new roman", 10),bd=5,relief=GROOVE)
        txt_expno.grid(row=2,column=1,pady=17,padx=17,sticky="w")
        # # # Batch
        lbl_batch = Label(Manage_Frame,text="Batch",fg="black",bg="yellow",font=("times new roman", 15))
        lbl_batch.grid(row=3,column=0,pady=17,padx=17,sticky="w")
        
        txt_batch = Entry(Manage_Frame,textvariable=self.Batch_var,font=("times new roman", 10),bd=5,relief=GROOVE)
        txt_batch.grid(row=3,column=1,pady=17,padx=17,sticky="w")
        # # # Roll No
        lbl_rollno = Label(Manage_Frame,text="Roll No",fg="black",bg="yellow",font=("times new roman", 15))
        lbl_rollno.grid(row=4,column=0,pady=17,padx=17,sticky="w")
        
        txt_Roll = Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman", 10),bd=5,relief=GROOVE)
        txt_Roll.grid(row=4,column=1,pady=17,padx=17,sticky="w")
        # # # Date of Starting Exp
        lbl_start = Label(Manage_Frame,text="Date of Starting Exp",fg="black",bg="yellow",font=("times new roman", 15))
        lbl_start.grid(row=5,column=0,pady=17,padx=17,sticky="w")
        
        txt_start = DateEntry(Manage_Frame,textvariable=self.DoSE_var,font=("times new roman", 10),bd=5,relief=GROOVE)
        txt_start.grid(row=5,column=1,pady=20,padx=20,sticky="w")
        # # # Date of Completion of Exp
        lbl_complete= Label(Manage_Frame,text="Date of Completion of Exp",fg="black",bg="yellow",font=("times new roman", 15))
        lbl_complete.grid(row=6,column=0,pady=17,padx=17,sticky="w")
        
        txt_complete = DateEntry(Manage_Frame,textvariable=self.DoCE_var,font=("times new roman", 10),bd=5,relief=GROOVE)
        txt_complete.grid(row=6,column=1,pady=17,padx=17,sticky="w")
        # # # Expected Date of Exp Checking
        lbl_check = Label(Manage_Frame,text="Expected Date of Checking",fg="black",bg="yellow",font=("times new roman", 15))
        lbl_check.grid(row=7,column=0,pady=17,padx=17,sticky="w")
        
        txt_check = DateEntry(Manage_Frame,textvariable=self.EDEC_var,font=("times new roman", 10),bd=5,relief=GROOVE)
        txt_check.grid(row=7,column=1,pady=17,padx=17,sticky="w")
        # # Date of Exp Checked
        lbl_fcheck = Label(Manage_Frame,text="Date of Exp Checked",fg="black",bg="yellow",font=("times new roman", 15))
        lbl_fcheck.grid(row=8,column=0,pady=17,padx=17,sticky="w")
        
        txt_fchecked = DateEntry(Manage_Frame,textvariable=self.DEC_var,font=("times new roman", 10),bd=5,relief=GROOVE)
        txt_fchecked.grid(row=8,column=1,pady=17,padx=17,sticky="w")
        # # Marks
        lbl_marks = Label(Manage_Frame,text="Marks",fg="black",bg="yellow",font=("times new roman", 15))
        lbl_marks.grid(row=9,column=0,pady=17,padx=17,sticky="w")
        
        txt_marks = Entry(Manage_Frame,textvariable=self.Marks_var,font=("times new roman", 10),bd=5,relief=GROOVE)
        txt_marks.grid(row=9,column=1,pady=17,padx=17,sticky="w")
        
        # BUTTON FRAME ===>
        
        Btn_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="yellow")
        Btn_Frame.place(x=10,y=723,width=450,height=65)

        Addbtn = Button(Btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=15,pady=15)
        Updbtn = Button(Btn_Frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=15,pady=15)
        Delbtn = Button(Btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=15,pady=15)
        Clrbtn = Button(Btn_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=15,pady=15)
        
        # DETAIL MANAGE FRAME ===>
        
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="yellow")
        Detail_Frame.place(x=475,y=90,width=1050,height=698)
        
        lbl_search = Label(Detail_Frame,text="Search By",bg="yellow",fg="black",font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0,column=0,padx=15,pady=15,sticky="w")
        
        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by,font=("times new roman",13,"bold"),state="readonly")
        combo_search['values'] = ("Roll_No", "Batch", "Exp_No")
        combo_search.grid(row=0,column=1,padx=30,pady=10)
        
        txt_search = Entry(Detail_Frame,textvariable=self.search_txt,width=35,font=("times new roman",13,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=10,sticky="w")

        searchBtn = Button(Detail_Frame,text="Search",width=15,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showAllBtn = Button(Detail_Frame,text="Show All",width=15,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)
        
        # TABLE FRAME ===>
        
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="yellow")
        Table_Frame.place(x=10,y=70,width=1020,height=603)
        
        scroll_x = Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_Table = ttk.Treeview(Table_Frame,columns=("Sr No","Exp No", "Batch", "Roll No", "Date of Starting Exp", "Date of Completion of Exp", "Expected Date of Checking", "Date of Exp Checked", "Marks"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_Table.xview)
        scroll_y.config(command=self.Student_Table.yview)
        self.Student_Table.heading("Sr No",text="Sr No")
        self.Student_Table.heading("Exp No",text="Exp No")
        self.Student_Table.heading("Batch",text="Batch")
        self.Student_Table.heading("Roll No",text="Roll No")
        self.Student_Table.heading("Date of Starting Exp",text="Date of Starting Exp")
        self.Student_Table.heading("Date of Completion of Exp",text="Date of Completion of Exp")
        self.Student_Table.heading("Expected Date of Checking",text="Expected Date of Checking")
        self.Student_Table.heading("Date of Exp Checked",text="Date of Exp Checked")
        self.Student_Table.heading("Marks",text="Marks")
        self.Student_Table['show'] = "headings"
        self.Student_Table.column("Sr No", width=100)
        self.Student_Table.column("Exp No", width=100)
        self.Student_Table.column("Batch", width=100)
        self.Student_Table.column("Roll No", width=100)
        self.Student_Table.column("Date of Starting Exp", width=200)
        self.Student_Table.column("Date of Completion of Exp", width=200)
        self.Student_Table.column("Expected Date of Checking", width=200)
        self.Student_Table.column("Date of Exp Checked", width=200)
        self.Student_Table.column("Marks", width=100)

        self.Student_Table.pack(fill=BOTH,expand=1)
        self.Student_Table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
         
    def add_students(self):
      if self.Roll_No_var.get() == "" or self.Batch_var.get() == "":
          messagebox.showerror("Error","All fields are required!!!")
      else:    
        con = pymysql.connect(host="localhost",user="root",password="",database="ybook")
        cur = con.cursor()
        cur.execute("insert into lr values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.Sr_No_var.get(),self.Exp_No_var.get(),
                                                                                         self.Batch_var.get(),
                                                                                        self.Roll_No_var.get(),
                                                                                        self.DoSE_var.get(),
                                                                                        self.DoCE_var.get(),
                                                                                        self.EDEC_var.get(),
                                                                                        self.DEC_var.get(),
                                                                                        self.Marks_var.get()))
         
        con.commit()    
        self.fetch_data()  
        self.clear()                                                                         
        con.close()
        messagebox.showinfo("Success", "Record has been inserted")
      
    def fetch_data(self):
          con = pymysql.connect(host="localhost",user="root",password="",database="ybook")
          cur = con.cursor()
          cur.execute("select * from lr")
          rows = cur.fetchall()
          if len(rows) != 0:
              self.Student_Table.delete(*self.Student_Table.get_children())
              for row in rows:
                  self.Student_Table.insert('',END,values=row)
              con.commit()    
          con.close()    
          
    def clear(self):
         self.Sr_No_var.set("")
         self.Exp_No_var.set("")
         self.Batch_var.set("")
         self.Roll_No_var.set("")
         self.DoSE_var.set("")
         self.DoCE_var.set("")
         self.EDEC_var.set("")
         self.DEC_var.set("")
         self.Marks_var.set("")
         
    def get_cursor(self,ev):
        cursor_row = self.Student_Table.focus()          
        content = self.Student_Table.item(cursor_row)
        row = content['values']
        self.Sr_No_var.set(row[0])
        self.Exp_No_var.set(row[1])
        self.Batch_var.set(row[2])
        self.Roll_No_var.set(row[3])
        self.DoSE_var.set(row[4])
        self.DoCE_var.set(row[5])
        self.EDEC_var.set(row[6])
        self.DEC_var.set(row[7])
        self.Marks_var.set(row[8]) 
        
    def update_data(self):
        con = pymysql.connect(host="localhost",user="root",password="",database="ybook")
        cur = con.cursor()
        cur.execute("update lr set Exp_No=%s,Batch=%s,Roll_No=%s,Date_of_Starting_Exp=%s,Date_of_Completion_of_Exp=%s,Expected_Date_of_Checking=%s,Date_of_Exp_Checked=%s,Marks=%s where Sr_No=%s",(
                                                                                        self.Exp_No_var.get(),
                                                                                        self.Batch_var.get(),
                                                                                        self.Roll_No_var.get(),
                                                                                        self.DoSE_var.get(),
                                                                                        self.DoCE_var.get(),
                                                                                        self.EDEC_var.get(),
                                                                                        self.DEC_var.get(),
                                                                                        self.Marks_var.get(),
                                                                                        self.Sr_No_var.get()
                                                                                        ))
         
        con.commit()    
        self.fetch_data()  
        self.clear()                                                                         
        con.close()
        
        
    def delete_data(self):
          con = pymysql.connect(host="localhost",user="root",password="",database="ybook")
          cur = con.cursor()
          cur.execute("delete from lr where Sr_No=%s", self.Sr_No_var.get())
          con.commit()
          con.close()
          self.fetch_data()  
          self.clear()         
          
    def search_data(self):
                        
          con = pymysql.connect(host="localhost",user="root",password="",database="ybook")
          cur = con.cursor()
          cur.execute("select * from lr where " + str(self.search_by.get()) + " LIKE  '%" +str(self.search_txt.get())+"%'")
          rows = cur.fetchall()
          if len(rows) != 0:
              self.Student_Table.delete(*self.Student_Table.get_children())
              for row in rows:
                  self.Student_Table.insert('',END,values=row)
              con.commit()     
          con.close()      
          
                                                                          
          

root = Tk()    
ob = Student(root)
root.mainloop()