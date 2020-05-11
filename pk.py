from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1550x900")
        
        
        title=Label(self.root,text="Student Database Management System",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="dark slate grey",fg="white")
        title.pack(side=TOP,fill=X)
        
        
   
        
        #variables
        
        self.Roll_no_var=StringVar()
        self.name_var=StringVar()
        self.add_var=StringVar()
        self.sex_var=StringVar()
        self.dob_var=StringVar()
        self.state_var=StringVar()
        self.mobile_var=StringVar()
        self.email_var=StringVar()
        self.search_by_var=StringVar()
        self.search_txt_var=StringVar()

        
        F1=Frame(self.root,bd=4,relief=RIDGE,bg="dark slate grey")
        F1.place(x=10,y=100,width=450,height=600)
        
        m_title=Label(F1,text="Manage Students",font=("times new roman",20,"bold"),bg="crimson",fg="white")
        m_title.grid(row=0,column=0,pady=10)
        
        lbl_roll=Label(F1,text="Roll No",font=("times new roman",18,"bold"),bg="crimson",fg="white")
        lbl_roll.grid(row=1,column=0,pady=5,padx=5,sticky="w")
        
        txt_roll=Entry(F1,font=("times new roman",12,"bold"),textvariable=self.Roll_no_var,relief=GROOVE,bd=5)
        txt_roll.grid(row=1,column=1,pady=5,padx=5,sticky="w")
        
        lbl_name=Label(F1,text="Name",font=("times new roman",18,"bold"),bg="crimson",fg="white")
        lbl_name.grid(row=2,column=0,pady=5,padx=5,sticky="w")
        
        txt_name=Entry(F1,textvariable=self.name_var,relief=GROOVE,bd=5,font=("times new roman",12,"bold"))
        txt_name.grid(row=2,column=1,pady=5,padx=5,sticky="w")
        
        lbl_DOB=Label(F1,text="DOB",font=("times new roman",18,"bold"),bg="crimson",fg="white")
        lbl_DOB.grid(row=3,column=0,pady=5,padx=5,sticky="w")
        
        txt_Dob=Entry(F1,textvariable=self.dob_var,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
        txt_Dob.grid(row=3,column=1,pady=5,padx=5,sticky="w")
        
        lbl_gender=Label(F1,text="Gender",font=("times new roman",18,"bold"),bg="crimson",fg="white")
        lbl_gender.grid(row=4,column=0,pady=5,padx=5,sticky="w")
        
        combo_gender=ttk.Combobox(F1,width=18,textvariable=self.sex_var,font=("times new roman",12,"bold"),state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=5,pady=5)
        
        lbl_Add=Label(F1,text="Address",font=("times new roman",18,"bold"),bg="crimson",fg="white")
        lbl_Add.grid(row=5,column=0,pady=5,padx=5,sticky="w")
        
        txt_add=Entry(F1,textvariable=self.add_var,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
        txt_add.grid(row=5,column=1,pady=5,padx=5,sticky="w")
        
        
        
        lbl_state=Label(F1,text="State",font=("times new roman",18,"bold"),bg="crimson",fg="white")
        lbl_state.grid(row=6,column=0,pady=5,padx=5,sticky="w")
        
        txt_state=Entry(F1,textvariable=self.state_var,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
        txt_state.grid(row=6,column=1,pady=5,padx=5,sticky="w")
        
        lbl_email=Label(F1,text="Email",font=("times new roman",18,"bold"),bg="crimson",fg="white")
        lbl_email.grid(row=7,column=0,pady=5,padx=5,sticky="w")
        
        txt_email=Entry(F1,textvariable=self.email_var,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
        txt_email.grid(row=7,column=1,pady=5,padx=5,sticky="w")
        
        lbl_phn=Label(F1,text="Mobile No",font=("times new roman",18,"bold"),bg="crimson",fg="white")
        lbl_phn.grid(row=8,column=0,pady=5,padx=5,sticky="w")
        
        txt_phone=Entry(F1,textvariable=self.mobile_var,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
        txt_phone.grid(row=8,column=1,pady=5,padx=5,sticky="w")
        
        #BUtton
        F3=Frame(F1,bd=4,relief=RIDGE,bg="black",padx=10)
        F3.place(x=15,y=530,width=420)
        
        
        
    
        
        
        
        Addbtn=Button(F3,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=5)
        Uptbtn=Button(F3,text="Update",width=10,command=self.update_detail).grid(row=0,column=1,padx=10,pady=5)
        Delebtn=Button(F3,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=5)
        Cletn=Button(F3,text="Clear",command= self.clear,width=10).grid(row=0,column=3,padx=10,pady=5)
        
        
        
        
        F2=Frame(self.root,bd=4,relief=RIDGE,bg="dark slate grey")
        F2.place(x=500,y=100,width=830,height=600)
        
        lbl_sear=Label(F2,text="Search By",font=("times new roman",18,"bold"),bg="crimson",fg="white")
        lbl_sear.grid(row=0,column=0,pady=10,padx=20,sticky="w")
        
        combo_sear=ttk.Combobox(F2,width=10,textvariable=self.search_by_var,font=("times new roman",12,"bold"),state="readonly")
        combo_sear["value"]=("RollNo","Name")
        combo_sear.grid(row=0,column=1,padx=10,pady=10)
        
        txt_sear=Entry(F2,width=15,textvariable=self.search_txt_var,font=("times new roman",10,"bold"),relief=GROOVE,bd=5)
        txt_sear.grid(row=0,column=2,pady=10,padx=20,sticky="w")
      
        searbtn=Button(F2,text="Search",width=10,command=self.search_data).grid(row=0,column=3,padx=10,pady=5)
        showalltn=Button(F2,text="ShowAll",width=10,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=5)
    
        
        
        
        F4=Frame(F2,bd=4,relief=RIDGE,bg="dark slate grey")
        F4.place(x=10,y=55,width=760,height=400)   
        scroll_x=Scrollbar(F4,orient=HORIZONTAL)
        scroll_y=Scrollbar(F4,orient=VERTICAL)
        
        self.Student_table=ttk.Treeview(F4,columns=("Roll","Name","DOB","Gender","Address","State","Email","Mobile"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)

        #table
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("Roll",text="Roll No.")
        self.Student_table.heading("Name",text="Name")
        self.Student_table.heading("DOB",text="DOB")
        self.Student_table.heading("Gender",text="Gender")
        self.Student_table.heading("Address",text="Address")
        self.Student_table.heading("State",text="State")
        self.Student_table.heading("Email",text="Email")
        self.Student_table.heading("Mobile",text="Mobile No.")
        self.Student_table['show']="headings"
        self.Student_table.column("Roll",width=100)
        self.Student_table.column("DOB",width=100)
        self.Student_table.column("Mobile",width=100)
        self.Student_table.column("Address",width=170)
        self.Student_table.column("Gender",width=100)
        self.Student_table.column("State",width=100)
        self.Student_table.column("Name",width=100)
        self.Student_table.column("Email",width=140)
        self.Student_table.bind("<ButtonRelease-1>",self.get_pointer)
        
        
        self.Student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        
        lbl_det=Label(F2,text="Other Details",font=("times new roman",18,"bold"),bg="crimson",fg="white")
        lbl_det.place(x=20,y=480)
        
        
        
        #tableBUtton
        
        
        F5=Frame(F2,bd=4,relief=RIDGE,bg="black",padx=10)
        F5.place(x=130,y=530,width=430)
        
    
        
        Parbtn=Button(F5,text="Parents",width=15,command=self.parent1).grid(row=0,column=0,padx=10,pady=3)
        Admbtn=Button(F5,text="Admission",width=15,command=self.admission1).grid(row=0,column=1,padx=10,pady=3)
        Sectn=Button(F5,text="Section",width=15,command=self.section1).grid(row=0,column=2,padx=10,pady=3)
        
    def add_students(self):
        if self.Roll_no_var.get()=="" or self.name_var.get()=="" or self.dob_var.get()=="" or self.sex_var.get()=="" or self.add_var.get()=="" or self.state_var.get()=="" or self.email_var.get()=="" or self.mobile_var.get()=="" :
            messagebox.showerror("Error","All Fields Are Required!!!")
        else:
            R=self.Roll_no_var.get()
            N=self.name_var.get()
            D = self.dob_var.get()
            G=self.sex_var.get()
            A=self.add_var.get()
            S=self.state_var.get()
            E=self.email_var.get()
            M=self.mobile_var.get()
            con=cx_Oracle.connect("system/Prince")
            cur=con.cursor()
            cur.execute("INSERT INTO Students(RollNo,Name,DOB,Gender,Address,State,Email,MobileNo)VALUES(:1,:2,:3,:4,:5,:6,:7,:8)", (R,N,D,G,A,S,E,M))
                                                                                
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been Added Successfully")

    def fetch_data(self):
        con=cx_Oracle.connect("system/Prince")
        cur=con.cursor()
        cur.execute("select * from Students")
        rows = cur.fetchall()
        if (rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()




    def clear(self):
         if self.Roll_no_var.get()=="" or self.name_var.get()=="" or self.dob_var.get()=="" or self.sex_var.get()=="" or self.add_var.get()=="" or self.state_var.get()=="" or self.email_var.get()=="" or self.mobile_var.get()=="" :
            messagebox.showerror("Error","All Fields Are Required!!!")
         else:
            self.Roll_no_var.set('')
            self.name_var.set('')
            self.dob_var.set('')
            self.sex_var.set('')
            self.add_var.set('')
            self.state_var.set('')
            self.email_var.set('')
            self.mobile_var.set('')
            messagebox.showinfo("Success","Record Cleared Successfully")


    def get_pointer(self,event):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.Roll_no_var.set(row[0])
        self.name_var.set(row[1])
        self.dob_var.set(row[2])
        self.sex_var.set(row[3])
        self.add_var.set(row[4])
        self.state_var.set(row[5])
        self.email_var.set(row[6])
        self.mobile_var.set(row[7])

    def update_detail(self):
        R=self.Roll_no_var.get()
        N=self.name_var.get()
        D = self.dob_var.get()
        G=self.sex_var.get()
        A=self.add_var.get()
        S=self.state_var.get()
        E=self.email_var.get()
        M=self.mobile_var.get()
        con=cx_Oracle.connect("system/Prince")
        cur=con.cursor()
        sql="UPDATE Students SET Name=:2,Gender=:4,Address=:5,State=:6,Email=:7,MobileNo=:8 where RollNo=:1"
        cur.execute(sql,(N,G,A,S,E,M,R))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()


    def delete_data(self):
        con=cx_Oracle.connect("system/Prince")
        cur=con.cursor()
        cur.execute("Delete From  Students where RollNo='%s'"%self.Roll_no_var.get())
        #rows = cur.fetchall()
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con=cx_Oracle.connect("system/Prince")
        cur=con.cursor()
        
        cur.execute("select * from Students where "+str(self.search_by_var.get())+" LIKE '%"+str(self.search_txt_var.get()+"%'"))
        rows = cur.fetchall()
        if (rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def parent1(self):
        from parentsnew import Parent 
        root1=Toplevel()
        obj=Parent(root1)
        root1.mainloop()

    def admission1(self):
        from admission import Admission
        root2=Toplevel()
        ob2=Admission(root2)
        root2.mainloop()

    def section1(self):
        from section import Section
        root3=Toplevel()
        ob3=Section(root3)
        root3.mainloop()



    #parents
    

        
    
root=Tk()
ob=Student(root)
root.mainloop()




