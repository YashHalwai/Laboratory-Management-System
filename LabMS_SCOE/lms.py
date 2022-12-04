from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas

# functionality part

# Exit
def iexit():
    result = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

# Export Data
def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')
    indexing = studentTable.get_children()
    newList=[]
    for index in indexing:
        content=studentTable.item(index)
        dataList=content['values']
        newList.append(dataList)

    table = pandas.DataFrame(newList,columns=['SrNo','Exp No','Batch','Roll No','PRN','Name of the Student','Start Date','End Date','Writeup Checking Date','Performance (4)',
                                 'Understanding (4)','Timely Submission (2)','Total Marks (10)'])
    table.to_csv(url,index = False)
    messagebox.showinfo('Success','Data is saved successfully')


# Update Student
def update_student():
    def update_data():
        query = 'update student set ExpNo =%s,Batch = %s, RollNo = %s, PRN = %s,NameOfTheStudent = %s,StartDate = %s,EndDate = %s,WriteupCheckingDate = %s,Performance = %s,Understanding = %s,TimelySubmission = %s, TotalMarks = %s where SrNo = %s'
        mycursor.execute(query,(ExpNoEntry.get(), BatchEntry.get(), idEntry.get(),PRNEntry.get(),NameEntry.get(),SDateEntry.get(),EDateEntry.get(),WriteUpCDDateEntry.get(),PEntry.get(),UEntry.get(),TSEntry.get(),TMEntry.get(),SrNoEntry.get()))
        con.commit()
        messagebox.showinfo('Success',f' Roll No {idEntry.get()} is modified successfully')
        update_window.destroy()
        show_student()

    update_window = Toplevel()
    update_window.title('Update Student')
    update_window.grab_set()
    update_window.resizable(False, False)

    SrNoLabel = Label(update_window, text='Sr No', font=('times new roman', 15, 'bold'))
    SrNoLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    SrNoEntry = Entry(update_window, font=('times new roman', 10, 'bold'), width=24)
    SrNoEntry.grid(row=0, column=1, pady=15, padx=10)

    ExpNoLabel = Label(update_window, text='Exp No', font=('times new roman', 15, 'bold'))
    ExpNoLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    ExpNoEntry = Entry(update_window, font=('times new roman', 10, 'bold'), width=24)
    ExpNoEntry.grid(row=0, column=1, pady=15, padx=10)

    BatchLabel = Label(update_window, text='Batch', font=('times new roman', 15, 'bold'))
    BatchLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    BatchEntry = Entry(update_window, font=('times new roman', 10, 'bold'), width=24)
    BatchEntry.grid(row=1, column=1, pady=15, padx=10)

    idLabel = Label(update_window, text='Roll No', font=('times new roman', 15, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(update_window, font=('times new roman', 10, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    PRNLabel = Label(update_window, text='P R N', font=('times new roman', 15, 'bold'))
    PRNLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    PRNEntry = Entry(update_window, font=('times new roman', 10, 'bold'), width=24)
    PRNEntry.grid(row=1, column=1, pady=15, padx=10)

    NameLabel = Label(update_window, text='Name of the Student', font=('times new roman', 15, 'bold'))
    NameLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    NameEntry = Entry(update_window, font=('times new roman', 10, 'bold'), width=24)
    NameEntry.grid(row=2, column=1, pady=15, padx=10)

    SDateLabel = Label(update_window, text='Start Date', font=('times new roman', 15, 'bold'))
    SDateLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    SDateEntry = Entry(update_window, font=('times new roman', 10, 'bold'), width=24)
    SDateEntry.grid(row=3, column=1, pady=15, padx=10)

    EDateLabel = Label(update_window, text='End Date', font=('times new roman', 15, 'bold'))
    EDateLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    EDateEntry = Entry(update_window, font=('times new roman', 10, 'bold'), width=24)
    EDateEntry.grid(row=4, column=1, pady=15, padx=10)

    WriteUpCDDateLabel = Label(update_window, text='Writeup Checking Date', font=('times new roman', 15, 'bold'))
    WriteUpCDDateLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    WriteUpCDDateEntry = Entry(update_window, font=('times new roman', 10, 'bold'), width=24)
    WriteUpCDDateEntry.grid(row=5, column=1, pady=15, padx=10)

    PLabel = Label(update_window, text='Performance (4)', font=('times new roman', 15, 'bold'))
    PLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    PEntry = Entry(update_window, font=('times new roman', 10, 'bold'), width=24)
    PEntry.grid(row=6, column=1, pady=15, padx=10)

    ULabel = Label(update_window, text='Understanding (4)', font=('times new roman', 15, 'bold'))
    ULabel.grid(row=7, column=0, padx=30, pady=15, sticky=W)
    UEntry = Entry(update_window, font=('times new roman', 10, 'bold'), width=24)
    UEntry.grid(row=7, column=1, pady=15, padx=10)

    TSLabel = Label(update_window, text='Timely Submission (2)', font=('times new roman', 15, 'bold'))
    TSLabel.grid(row=8, column=0, padx=30, pady=15, sticky=W)
    TSEntry = Entry(update_window, font=('times new roman', 10, 'bold'), width=24)
    TSEntry.grid(row=8, column=1, pady=15, padx=10)

    TMLabel = Label(update_window, text='Total Marks (10)', font=('times new roman', 15, 'bold'))
    TMLabel.grid(row=9, column=0, padx=30, pady=15, sticky=W)
    TMEntry = Entry(update_window, font=('times new roman', 10, 'bold'), width=24)
    TMEntry.grid(row=9, column=1, pady=15, padx=10)

    search_student_button = ttk.Button(update_window, text='Update Student',command=update_data)
    search_student_button.grid(row=10, columnspan=2, pady=10)

    indexing = studentTable.focus()
    print(indexing)
    content = studentTable.item(indexing)
    listData = content['values']
    # print(listDat)
    SrNoEntry.insert(0, listData[0])
    ExpNoEntry.insert(0, listData[0])
    BatchEntry.insert(0, listData[1])
    idEntry.insert(0, listData[2])
    PRNEntry.insert(0, listData[3])
    NameEntry.insert(0, listData[4])
    SDateEntry.insert(0, listData[5])
    EDateEntry.insert(0, listData[6])
    WriteUpCDDateEntry.insert(0, listData[7])
    PEntry.insert(0, listData[8])
    UEntry.insert(0, listData[9])
    TSEntry.insert(0, listData[10])
    TMEntry.insert(0, listData[11])



# Show Student
def show_student():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)

# Delete Student

def delete_student():
    indexing = studentTable.focus()
    print(indexing)
    content = studentTable.item(indexing)
    content_id=content['values'][0]
    query='delete from student where RollNo = %s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'RollNo {content_id} is deleted successfully')
    query='select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)

# Search Student
def search_student():

    def search_data():
        query = 'select * from student where SrNo = %s or ExpNo =%s or Batch = %s or RollNo = %s or PRN = %s or NameOfTheStudent = %s or StartDate = %s or EndDate = %s or WriteupCheckingDate = %s or Performance = %s or Understanding = %s or TimelySubmission = %s or TotalMarks = %s'
        mycursor.execute(query,(SrNoEntry.get(), ExpNoEntry.get(), BatchEntry.get(), idEntry.get(),PRNEntry.get(),NameEntry.get(),SDateEntry.get(),EDateEntry.get(),WriteUpCDDateEntry.get(),PEntry.get(),UEntry.get(),TSEntry.get(),TMEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data = mycursor.fetchall()
        for data in fetched_data:
            studentTable.insert('',END,values=data)


    search_window = Toplevel()
    search_window.title('Search Student')
    search_window.grab_set()
    search_window.resizable(False, False)

    SrNoLabel = Label(search_window, text='Sr No', font=('times new roman', 15, 'bold'))
    SrNoLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    SrNoEntry = Entry(search_window, font=('times new roman', 10, 'bold'), width=24)
    SrNoEntry.grid(row=0, column=1, pady=15, padx=10)

    ExpNoLabel = Label(search_window, text='Exp No', font=('times new roman', 15, 'bold'))
    ExpNoLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    ExpNoEntry = Entry(search_window, font=('times new roman', 10, 'bold'), width=24)
    ExpNoEntry.grid(row=0, column=1, pady=15, padx=10)

    BatchLabel = Label(search_window, text='Batch', font=('times new roman', 15, 'bold'))
    BatchLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    BatchEntry = Entry(search_window, font=('times new roman', 10, 'bold'), width=24)
    BatchEntry.grid(row=1, column=1, pady=15, padx=10)

    idLabel = Label(search_window, text='Roll No', font=('times new roman', 15, 'bold'))
    idLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(search_window, font=('times new roman', 10, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    PRNLabel = Label(search_window, text='PRN', font=('times new roman', 15, 'bold'))
    PRNLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    PRNEntry = Entry(search_window, font=('times new roman', 10, 'bold'), width=24)
    PRNEntry.grid(row=1, column=1, pady=15, padx=10)

    NameLabel = Label(search_window, text='Name of the Student', font=('times new roman', 15, 'bold'))
    NameLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    NameEntry = Entry(search_window, font=('times new roman', 10, 'bold'), width=24)
    NameEntry.grid(row=2, column=1, pady=15, padx=10)

    SDateLabel = Label(search_window, text='Start Date', font=('times new roman', 15, 'bold'))
    SDateLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    SDateEntry = Entry(search_window, font=('times new roman', 10, 'bold'), width=24)
    SDateEntry.grid(row=3, column=1, pady=15, padx=10)

    EDateLabel = Label(search_window, text='End Date', font=('times new roman', 15, 'bold'))
    EDateLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    EDateEntry = Entry(search_window, font=('times new roman', 10, 'bold'), width=24)
    EDateEntry.grid(row=4, column=1, pady=15, padx=10)

    WriteUpCDDateLabel = Label(search_window, text='Writeup Checking Date', font=('times new roman', 15, 'bold'))
    WriteUpCDDateLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    WriteUpCDDateEntry = Entry(search_window, font=('times new roman', 10, 'bold'), width=24)
    WriteUpCDDateEntry.grid(row=5, column=1, pady=15, padx=10)

    PLabel = Label(search_window, text='Performance (4)', font=('times new roman', 15, 'bold'))
    PLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    PEntry = Entry(search_window, font=('times new roman', 10, 'bold'), width=24)
    PEntry.grid(row=6, column=1, pady=15, padx=10)

    ULabel = Label(search_window, text='Understanding (4)', font=('times new roman', 15, 'bold'))
    ULabel.grid(row=7, column=0, padx=30, pady=15, sticky=W)
    UEntry = Entry(search_window, font=('times new roman', 10, 'bold'), width=24)
    UEntry.grid(row=7, column=1, pady=15, padx=10)

    TSLabel = Label(search_window, text='Timely Submission (2)', font=('times new roman', 15, 'bold'))
    TSLabel.grid(row=8, column=0, padx=30, pady=15, sticky=W)
    TSEntry = Entry(search_window, font=('times new roman', 10, 'bold'), width=24)
    TSEntry.grid(row=8, column=1, pady=15, padx=10)

    TMLabel = Label(search_window, text='Total Marks (10)', font=('times new roman', 15, 'bold'))
    TMLabel.grid(row=9, column=0, padx=30, pady=15, sticky=W)
    TMEntry = Entry(search_window, font=('times new roman', 10, 'bold'), width=24)
    TMEntry.grid(row=9, column=1, pady=15, padx=10)

    search_student_button = ttk.Button(search_window, text='Search Student', command=search_data)
    search_student_button.grid(row=10, columnspan=2, pady=10)

# Add Student
def add_student():
     def add_data():
        if SrNoEntry.get() == '' or ExpNoEntry.get == '' or BatchEntry.get == '' or idEntry.get == '' or PRNEntry.get == '' or NameEntry == '' or SDateEntry == '' or EDateEntry == '' or WriteUpCDDateEntry == '' or PEntry == '' or UEntry == '' or TSEntry == '' or TMEntry == '':
            messagebox.showerror('Error', 'All fields are required', parent=add_window)
        else:
            try:
              query = 'insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
              mycursor .execute(query,(SrNoEntry.get(),ExpNoEntry.get(),BatchEntry.get(),idEntry.get(),PRNEntry.get(),NameEntry.get(),SDateEntry.get(),EDateEntry.get(),WriteUpCDDateEntry.get(),PEntry.get(),UEntry.get(),TSEntry.get(),TMEntry.get()))
              con.commit()
              result = messagebox.askyesno('Confirm','Data added successfully. Do you want to clean form?',parent = add_window)
              if result:
                SrNoEntry.delete(0,END)
                ExpNoEntry.delete(0,END)
                BatchEntry.delete(0,END)
                idEntry.delete(0,END)
                PRNEntry.delete(0,END)
                NameEntry.delete(0,END)
                SDateEntry.delete(0,END)
                EDateEntry.delete(0,END)
                WriteUpCDDateEntry.delete(0,END)
                PEntry.delete(0,END)
                UEntry.delete(0,END)
                TSEntry.delete(0,END)
                TMEntry.delete(0,END)
              else:
                pass
            except:
              messagebox.showerror('Error','Id Cannot be repeated', parent=add_window)
              return

            query = 'select * from student'
            mycursor.execute(query)
            fetched_data = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            # print(fetched_data)

            for data in fetched_data:
                studentTable.insert('', END, values=data)

     add_window = Toplevel()
     add_window.grab_set()
     add_window.resizable(False,False)

     SrNoLabel = Label(add_window, text='Sr No', font=('times new roman', 15, 'bold'))
     SrNoLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
     SrNoEntry = Entry(add_window, font=('times new roman', 10, 'bold'), width=24)
     SrNoEntry.grid(row=0, column=1, pady=15, padx=10)

     ExpNoLabel = Label(add_window, text='Exp No', font=('times new roman', 15, 'bold'))
     ExpNoLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
     ExpNoEntry = Entry(add_window, font=('times new roman', 10, 'bold'), width=24)
     ExpNoEntry.grid(row=1, column=1, pady=15, padx=10)

     BatchLabel = Label(add_window, text='Batch', font=('times new roman', 15, 'bold'))
     BatchLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
     BatchEntry = Entry(add_window, font=('times new roman', 10, 'bold'), width=24)
     BatchEntry.grid(row=2, column=1, pady=15, padx=10)

     idLabel = Label(add_window,text='Roll No',font=('times new roman',15, 'bold'))
     idLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
     idEntry = Entry(add_window,font=('times new roman', 10, 'bold'),width=24)
     idEntry.grid(row=3,column=1,pady=15,padx=10)

     PRNLabel = Label(add_window, text='PRN', font=('times new roman', 15, 'bold'))
     PRNLabel.grid(row=4, column=0, padx=30, pady=15,sticky=W)
     PRNEntry = Entry(add_window, font=('times new roman', 10, 'bold'), width=24)
     PRNEntry.grid(row=4, column=1, pady=15, padx=10)

     NameLabel = Label(add_window, text='Name of the Student', font=('times new roman', 15, 'bold'))
     NameLabel.grid(row=5, column=0, padx=30, pady=15,sticky=W)
     NameEntry = Entry(add_window, font=('times new roman', 10, 'bold'), width=24)
     NameEntry.grid(row=5, column=1, pady=15, padx=10)

     SDateLabel = Label(add_window, text='Start Date', font=('times new roman', 15, 'bold'))
     SDateLabel.grid(row=6, column=0, padx=30, pady=15,sticky=W)
     SDateEntry = Entry(add_window, font=('times new roman', 10, 'bold'), width=24)
     SDateEntry.grid(row=6, column=1, pady=15, padx=10)

     EDateLabel = Label(add_window, text='End Date', font=('times new roman', 15, 'bold'))
     EDateLabel.grid(row=7, column=0, padx=30, pady=15,sticky=W)
     EDateEntry = Entry(add_window, font=('times new roman', 10, 'bold'), width=24)
     EDateEntry.grid(row=7, column=1, pady=15, padx=10)

     WriteUpCDDateLabel = Label(add_window, text='Writeup Checking Date', font=('times new roman', 15, 'bold'))
     WriteUpCDDateLabel.grid(row=8, column=0, padx=30, pady=15,sticky=W)
     WriteUpCDDateEntry = Entry(add_window, font=('times new roman', 10, 'bold'), width=24)
     WriteUpCDDateEntry.grid(row=8, column=1, pady=15, padx=10)

     PLabel = Label(add_window, text='Performance (4)', font=('times new roman', 15, 'bold'))
     PLabel.grid(row=9, column=0, padx=30, pady=15,sticky=W)
     PEntry = Entry(add_window, font=('times new roman', 10, 'bold'), width=24)
     PEntry.grid(row=9, column=1, pady=15, padx=10)

     ULabel = Label(add_window, text='Understanding (4)', font=('times new roman', 15, 'bold'))
     ULabel.grid(row=10, column=0, padx=30, pady=15,sticky=W)
     UEntry = Entry(add_window, font=('times new roman', 10, 'bold'), width=24)
     UEntry.grid(row=10, column=1, pady=15, padx=10)

     TSLabel = Label(add_window, text='Timely Submission (2)', font=('times new roman', 15, 'bold'))
     TSLabel.grid(row=11, column=0, padx=30, pady=15,sticky=W)
     TSEntry = Entry(add_window, font=('times new roman', 10, 'bold'), width=24)
     TSEntry.grid(row=11, column=1, pady=15, padx=10)

     TMLabel = Label(add_window, text='Total Marks (10)', font=('times new roman', 15, 'bold'))
     TMLabel.grid(row=12, column=0, padx=30, pady=15,sticky=W)
     TMEntry = Entry(add_window, font=('times new roman', 10, 'bold'), width=24)
     TMEntry.grid(row=12, column=1, pady=15, padx=10)

     add_student_button = ttk.Button(add_window,text = 'Add Student',command=add_data)
     add_student_button.grid(row=13,columnspan=2,pady=10)



def connect_database():
    def connect():
        global mycursor,con
        try:
            con=pymysql.connect(host='localhost',user='root',password='12345')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return

        try:
            query='create laboratoryms'
            mycursor.execute(query)
            query='use laboratoryms'
            mycursor.execute(query)
            query='create table student(SrNo int not null primary key, ExpNo int, Batch varchar(3), RollNo int, PRN varchar(11),NameOfTheStudent varchar(100),StartDate varchar(30),' \
                  'EndDate varchar(100),WriteupCheckingDate varchar(20),Performance int,Understanding int, TimelySubmission int, TotalMarks int)'
            mycursor.execute(query)
        except:
            query='use laboratoryms'
            mycursor.execute(query)
        messagebox.showinfo('Success', 'Database Connection is successful', parent=connectWindow)
        connectWindow.destroy()
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
        exitButton.config(state=NORMAL)


    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',20,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel = Label(connectWindow, text='User Name', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)

    usernameEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)

# SLIDER
count=0
text=''
def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(300,slider)

# CLOCK
def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000,clock)


root = ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')

root.geometry('1174x680+0+0')
root.resizable(0,0)
root.title('Laboratory Management System')


datetimeLabel=Label(root,font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()


s='Laboratory Management System' #s[count]=t when count is 1
sliderLabel=Label(root,font=('arial',28,'italic bold'),width=30)
sliderLabel.place(x=200,y=0)
slider()


connectButton=ttk.Button(root,text='Connect database',command=connect_database)
connectButton.place(x=980,y=0)

# LEFT FAME

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=PhotoImage(file='college.png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)

addstudentButton=ttk.Button(leftFrame,text='Add Student',width=25,state=DISABLED, command=add_student)
addstudentButton.grid(row=1,column=0,pady=20)

searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=25,state=DISABLED,command=search_student)
searchstudentButton.grid(row=2,column=0,pady=20)

deletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=25,state=DISABLED,command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=20)

updatestudentButton=ttk.Button(leftFrame,text='Update Student',width=25,state=DISABLED,command=update_student)
updatestudentButton.grid(row=4,column=0,pady=20)

showstudentButton=ttk.Button(leftFrame,text='Show Student',width=25,state=DISABLED,command=show_student)
showstudentButton.grid(row=5,column=0,pady=20)

exportstudentButton=ttk.Button(leftFrame,text='Export data',width=25,state=DISABLED,command=export_data)
exportstudentButton.grid(row=6,column=0,pady=20)

exitButton=ttk.Button(leftFrame,text='Exit',width=25,state=DISABLED,command=iexit)
exitButton.grid(row=7,column=0,pady=20)

# RIGHT FRAME

rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,columns=('Sr No','Exp No','Batch','Roll No','PRN','Name of the Student','Start Date','End Date','Writeup Checking Date','Performance (4)',
                                 'Understanding (4)','Timely Submission (2)','Total Marks (10)'),
                          xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

studentTable.pack(expand=1,fill=BOTH)

studentTable.heading('Sr No',text='Sr No')
studentTable.heading('Exp No',text='Exp No')
studentTable.heading('Batch',text='Batch')
studentTable.heading('Roll No',text='Roll No')
studentTable.heading('PRN',text='PRN')
studentTable.heading('Name of the Student',text='Name of the Student')
studentTable.heading('Start Date',text='Start Date')
studentTable.heading('End Date',text='End Date')
studentTable.heading('Writeup Checking Date',text='Writeup Checking Date')
studentTable.heading('Performance (4)',text='Performance (4)')
studentTable.heading('Understanding (4)',text='Understanding (4)')
studentTable.heading('Timely Submission (2)',text='Timely Submission (2)')
studentTable.heading('Total Marks (10)',text='Total Marks (10)')

studentTable.column('Sr No',width=100,anchor=CENTER)
studentTable.column('Exp No',width=100,anchor=CENTER)
studentTable.column('Batch',width=100,anchor=CENTER)
studentTable.column('Roll No',width=100,anchor=CENTER)
studentTable.column('PRN',width=250,anchor=CENTER)
studentTable.column('Name of the Student',width=400,anchor=CENTER)
studentTable.column('Start Date',width=150,anchor=CENTER)
studentTable.column('End Date',width=150,anchor=CENTER)
studentTable.column('Writeup Checking Date', width=250,anchor=CENTER)
studentTable.column('Performance (4)',width=200,anchor=CENTER)
studentTable.column('Understanding (4)',width=200,anchor=CENTER)
studentTable.column('Timely Submission (2)',width=200,anchor=CENTER)
studentTable.column('Total Marks (10)',width=200,anchor=CENTER)

style = ttk.Style()

# style.configure('Treeview',rowheight=40,font=('arial',12,'bold'),foreground='red4',background='yellow',fieldbackground='gray')
style.configure('Treeview',rowheight=40,font=('arial',12,'bold'))
style.configure('Treeview.Heading',font=('arial',12,'bold'))


studentTable.config(show='headings')

root.mainloop()