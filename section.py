from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle
class Section:

    def __init__(self,window3):
        self.window3=window3
        self.window3.title("Section Details")
        self.window3.geometry("1550x900")
        
        
        title=Label(self.window3,text="Section Detail",bd=10,relief=GROOVE,font=("times new roman",20,"bold"),bg="dark slate grey",fg="white")
        title.pack(side=TOP,fill=X)
        
        
        
        self.CLid_var=StringVar()
        self.Uroll_var=StringVar()
        self.Sname_var=StringVar()
        self.Tname_var=StringVar()
        self.Doj_var=StringVar()
        self.Doe_var=StringVar()
        self.search_byyy_var=StringVar()
        self.search_txxxt_var=StringVar()
        
        
        F1=Frame(window3,bd=4,relief=RIDGE,bg="dark slate grey")
        F1.place(x=10,y=70,width=450,height=600)
            
        m_title=Label(F1,text="Manage Section",font=("times new roman",20,"bold"),bg="crimson",fg="white")
        m_title.grid(row=0,column=0,pady=10)
            
        lbl_id=Label(F1,text="College ID",font=("times new roman",18,"bold"),bg="crimson",fg="white")
        lbl_id.grid(row=1,column=0,pady=5,padx=5,sticky="w")
            
        txt_id=Entry(F1,font=("times new roman",12,"bold"),textvariable=self.CLid_var,relief=GROOVE,bd=5)
        txt_id.grid(row=1,column=1,pady=5,padx=5,sticky="w")
        
        lbl_name=Label(F1,text="Name",font=("times new roman",18,"bold"),bg="crimson",fg="white")
        lbl_name.grid(row=3,column=0,pady=5,padx=5,sticky="w")
            
        txt_name=Entry(F1,textvariable=self.Sname_var,relief=GROOVE,bd=5,font=("times new roman",12,"bold"))
        txt_name.grid(row=3,column=1,pady=5,padx=5,sticky="w")
            
        lbl_roll_no=Label(F1,text="Roll No.",font=("times new roman",18,"bold"),bg="crimson",fg="white")
        lbl_roll_no.grid(row=2,column=0,pady=5,padx=5,sticky="w")
            
        txt_roll_no=Entry(F1,textvariable=self.Uroll_var,relief=GROOVE,bd=5,font=("times new roman",12,"bold"))
        txt_roll_no.grid(row=2,column=1,pady=5,padx=5,sticky="w")
        
        lbl_tname=Label(F1,text="Teacher Name",font=("times new roman",18,"bold"),bg="crimson",fg="white")
        lbl_tname.grid(row=4,column=0,pady=5,padx=5,sticky="w")
            
        txt_tname=Entry(F1,textvariable=self.Tname_var,relief=GROOVE,bd=5,font=("times new roman",12,"bold"))
        txt_tname.grid(row=4,column=1,pady=5,padx=5,sticky="w")
        
        lbl_date=Label(F1,text="Class Start Date",font=("times new roman",18,"bold"),bg="crimson",fg="white")
        lbl_date.grid(row=5,column=0,pady=5,padx=5,sticky="w")
            
        txt_date=Entry(F1,textvariable=self.Doj_var,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
        txt_date.grid(row=5,column=1,pady=5,padx=5,sticky="w")
            
        lbl_edate=Label(F1,text="Class End Date",font=("times new roman",18,"bold"),bg="crimson",fg="white")
        lbl_edate.grid(row=6,column=0,pady=5,padx=5,sticky="w")
        
        txt_edate=Entry(F1,textvariable=self.Doe_var,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
        txt_edate.grid(row=6,column=1,pady=5,padx=5,sticky="w")
            
            
        
        
        F3=Frame(F1,bd=4,relief=RIDGE,bg="black",padx=10)
        F3.place(x=15,y=450,width=420)
            
            
        Addbtn=Button(F3,text="Add",width=10,command=self.add_section).grid(row=0,column=0,padx=10,pady=5)
        Uptbtn=Button(F3,text="Update",width=10,command=self.update_d).grid(row=0,column=1,padx=10,pady=5)
        Delebtn=Button(F3,text="Delete",width=10,command=self.delete_da).grid(row=0,column=2,padx=10,pady=5)
        Cletn=Button(F3,text="Clear",width=10,command=self.clear_d).grid(row=0,column=3,padx=10,pady=5)
        
        
        
        F2=Frame(window3,bd=4,relief=RIDGE,bg="dark slate grey")
        F2.place(x=500,y=70,width=830,height=600)
            
        lbl_search=Label(F2,text="Search By",font=("times new roman",18,"bold"),bg="crimson",fg="white")
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")
            
        combo_search=ttk.Combobox(F2,width=10,font=("times new roman",12,"bold"),state="readonly",textvariable=self.search_byyy_var)
        combo_search["value"]=("COLLEGEID","Name")
        combo_search.grid(row=0,column=1,padx=10,pady=10)
            
        txt_search=Entry(F2,width=15,font=("times new roman",10,"bold"),relief=GROOVE,bd=5,textvariable=self.search_txxxt_var)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")
          
        searbtn=Button(F2,text="Search",width=10,command=self.search_da).grid(row=0,column=3,padx=10,pady=5)
        showalltn=Button(F2,text="ShowAll",width=10,command=self.fetch_d).grid(row=0,column=4,padx=10,pady=5)
        
        
        
        F4=Frame(F2,bd=4,relief=RIDGE,bg="dark slate grey")
        F4.place(x=10,y=55,width=760,height=400)   
        scroll_x=Scrollbar(F4,orient=HORIZONTAL)
        scroll_y=Scrollbar(F4,orient=VERTICAL)
            
        self.Section_table=ttk.Treeview(F4,columns=("AID","SNAME","CCODE","CNAME","DOA","Branch"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                    
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Section_table.xview)

            #table
        scroll_y.config(command=self.Section_table.yview)
        self.Section_table.heading("AID",text="College ID")
        self.Section_table.heading("SNAME",text="Roll No.")
        self.Section_table.heading("CCODE",text="Name")
        self.Section_table.heading("CNAME",text="Teacher Name")
        self.Section_table.heading("DOA",text="Class Start Date")
        self.Section_table.heading("Branch",text="Class End Date")
        self.Section_table['show']="headings"
        self.Section_table.column("AID",width=100)
        self.Section_table.column("SNAME",width=100)
        self.Section_table.column("CCODE",width=100)
        self.Section_table.column("CNAME",width=100)
        self.Section_table.column("DOA",width=100)
        self.Section_table.column("Branch",width=100)
        self.Section_table.bind("<ButtonRelease-1>",self.get_foc)
            
        self.Section_table.pack(fill=BOTH,expand=1)
        self.fetch_d()



    def add_section(self):
        J=self.CLid_var.get()
        T=self.Uroll_var.get()
        I=self.Sname_var.get()
        C=self.Tname_var.get()
        Z=self.Doj_var.get()
        K=self.Doe_var.get()
        if (J=="" or T=="" or I=="" or C=="" or Z=="" or K=="") :
               messagebox.showerror("Error","All Fields Are Required!!!")
        else:
             con=cx_Oracle.connect("system/Prince")
             cur=con.cursor()
             cur.execute("INSERT INTO Section(COLLEGEID,ROLLNO,NAME,TEACHERNAME,CLASSSTARTDATE,CLASSENDDATE)VALUES(:1,:2,:3,:4,:5,:6)", (J,T,I,C,Z,K))                                                               
             con.commit()
             self.fetch_d()
             messagebox.showinfo("Success","Record has been Added Successfull")
             self.clear_d()
             con.close()


             
    def fetch_d(self):
            con=cx_Oracle.connect("system/Prince")
            cur=con.cursor()
            cur.execute("select * from Section")
            rows = cur.fetchall()
            if (rows)!=0:
                self.Section_table.delete(*self.Section_table.get_children())
                for row in rows:
                    self.Section_table.insert('',END,values=row)
                con.commit()
            con.close()

    def clear_d(self):
            J=self.CLid_var.get()
            T=self.Uroll_var.get()
            I=self.Sname_var.get()
            C=self.Tname_var.get()
            Z=self.Doj_var.get()
            K=self.Doe_var.get()
            if (J=="" or T=="" or I=="" or C=="" or Z=="" or K=="") :
                  messagebox.showerror("Error","All Fields Are Required!!!")
            else:

                  self.CLid_var.set('')
                  self.Uroll_var.set('')
                  self.Sname_var.set('')
                  self.Tname_var.set('')
                  self.Doj_var.set('')
                  self.Doe_var.set('')
                  messagebox.showinfo("Success","Record Cleared Successfully")

    def get_foc(self,event):
            cursor_row=self.Section_table.focus()
            contents=self.Section_table.item(cursor_row)
            row=contents['values']
            self.CLid_var.set(row[0])
            self.Uroll_var.set(row[1])
            self.Sname_var.set(row[2])
            self.Tname_var.set(row[3])
            self.Doj_var.set(row[4])
            self.Doe_var.set(row[5])


    def update_d(self):
            J=self.CLid_var.get()
            T=self.Uroll_var.get()
            I=self.Sname_var.get()
            C=self.Tname_var.get()
            Z=self.Doj_var.get()
            K=self.Doe_var.get()
            con=cx_Oracle.connect("system/Prince")
            cur=con.cursor()
            sql="UPDATE Section SET ROLLNO=:2,NAME=:3,TEACHERNAME=:4 where COLLEGEID=:1"
            cur.execute(sql,(T,I,C,J))
            con.commit()
            self.fetch_d()
            messagebox.showinfo("Success","Record Updated Successfully")
            self.clear_d()
            con.close()
            


    def delete_da(self):
        con=cx_Oracle.connect("system/Prince")
        cur=con.cursor()
        cur.execute("Delete From  Section where COLLEGEID='%s'"%self.Clid_var.get())
        #rows = cur.fetchall()
        con.commit()
        con.close()
        self.fetch_d()
        self.clear_d()


    def search_da(self):
        con=cx_Oracle.connect("system/Prince")
        cur=con.cursor()
        
        cur.execute("select * from Section where "+str(self.search_byyy_var.get())+" LIKE '%"+str(self.search_txxxt_var.get()+"%'"))
        rows = cur.fetchall()
        if (rows)!=0:
            self.Section_table.delete(*self.Section_table.get_children())
            for row in rows:
                self.Section_table.insert('',END,values=row)
            con.commit()
        con.close()


    
    
    
    
    
    
    
    
if __name__ == "main":
    window3=Tk()
    ob=Section(window3)
    window3.mainloop()


# In[ ]:




