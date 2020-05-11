from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle
class Admission:
    def __init__(self,window2):
        self.window2=window2
        
        window2.title("Admission Details")
        window2.geometry("1550x900")
        
        
        title=Label(window2,text="Admission Detail",bd=10,relief=GROOVE,font=("times new roman",20,"bold"),bg="dark slate grey",fg="white")
        title.pack(side=TOP,fill=X)
        
        
        
        self.Adid_var=StringVar()
        self.Sname_var=StringVar()
        self.Ccode_var=StringVar()
        self.Cname_var=StringVar()
        self.Branch_var=StringVar()
        self.Doa_var=StringVar()
        self.search_byy_var=StringVar()
        self.search_txxt_var=StringVar()
        
        
        F1=Frame(window2,bd=4,relief=RIDGE,bg="dark slate grey")
        F1.place(x=10,y=70,width=450,height=600)
            
        m_title=Label(F1,text="Manage Admission",font=("times new roman",20,"bold"),bg="crimson",fg="white")
        m_title.grid(row=0,column=0,pady=10)
            
        lbl_admn=Label(F1,text="Admission ID",font=("times new roman",18,"bold"),bg="crimson",fg="white")
        lbl_admn.grid(row=1,column=0,pady=5,padx=5,sticky="w")
            
        txt_admn=Entry(F1,font=("times new roman",12,"bold"),textvariable=self.Adid_var,relief=GROOVE,bd=5)
        txt_admn.grid(row=1,column=1,pady=5,padx=5,sticky="w")
        
        lbl_Stname=Label(F1,text="Name",font=("times new roman",18,"bold"),bg="crimson",fg="white")
        lbl_Stname.grid(row=2,column=0,pady=5,padx=5,sticky="w")
            
        txt_Stname=Entry(F1,textvariable=self.Sname_var,relief=GROOVE,bd=5,font=("times new roman",12,"bold"))
        txt_Stname.grid(row=2,column=1,pady=5,padx=5,sticky="w")
            
        lbl_ccode=Label(F1,text="Course Code",font=("times new roman",18,"bold"),bg="crimson",fg="white")
        lbl_ccode.grid(row=3,column=0,pady=5,padx=5,sticky="w")
            
        txt_ccode=Entry(F1,textvariable=self.Ccode_var,relief=GROOVE,bd=5,font=("times new roman",12,"bold"))
        txt_ccode.grid(row=3,column=1,pady=5,padx=5,sticky="w")
        
        lbl_cname=Label(F1,text="Course Name",font=("times new roman",18,"bold"),bg="crimson",fg="white")
        lbl_cname.grid(row=4,column=0,pady=5,padx=5,sticky="w")
            
        txt_cname=Entry(F1,textvariable=self.Cname_var,relief=GROOVE,bd=5,font=("times new roman",12,"bold"))
        txt_cname.grid(row=4,column=1,pady=5,padx=5,sticky="w")
        
        lbl_bn=Label(F1,text="Branch",font=("times new roman",18,"bold"),bg="crimson",fg="white")
        lbl_bn.grid(row=5,column=0,pady=5,padx=5,sticky="w")
            
        txt_bn=Entry(F1,textvariable=self.Branch_var,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
        txt_bn.grid(row=5,column=1,pady=5,padx=5,sticky="w")
            
        lbl_DOA=Label(F1,text="Date Of Admission",font=("times new roman",18,"bold"),bg="crimson",fg="white")
        lbl_DOA.grid(row=6,column=0,pady=5,padx=5,sticky="w")
            
        txt_DOA=Entry(F1,textvariable=self.Doa_var,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
        txt_DOA.grid(row=6,column=1,pady=5,padx=5,sticky="w")
            
            
        
        
        F3=Frame(F1,bd=4,relief=RIDGE,bg="black",padx=10)
        F3.place(x=15,y=450,width=420)
            
            
        Addbtn=Button(F3,text="Add",width=10,command=self.add_admsn).grid(row=0,column=0,padx=10,pady=5)
        Uptbtn=Button(F3,text="Update",width=10,command=self.update_det).grid(row=0,column=1,padx=10,pady=5)
        Delebtn=Button(F3,text="Delete",width=10,command=self.delete_dat).grid(row=0,column=2,padx=10,pady=5)
        Cletn=Button(F3,text="Clear",width=10,command=self.clear_da).grid(row=0,column=3,padx=10,pady=5)
        
        
        
        F2=Frame(window2,bd=4,relief=RIDGE,bg="dark slate grey")
        F2.place(x=500,y=70,width=830,height=600)
            
        lbl_sear=Label(F2,text="Search By",font=("times new roman",18,"bold"),bg="crimson",fg="white")
        lbl_sear.grid(row=0,column=0,pady=10,padx=20,sticky="w")
            
        combo_sear=ttk.Combobox(F2,width=10,font=("times new roman",12,"bold"),textvariable=self.search_byy_var,state="readonly")
        combo_sear["value"]=("ADMISSIONID","Name")
        combo_sear.grid(row=0,column=1,padx=10,pady=10)
            
        txt_sear=Entry(F2,width=15,font=("times new roman",10,"bold"),relief=GROOVE,bd=5,textvariable=self.search_txxt_var)
        txt_sear.grid(row=0,column=2,pady=10,padx=20,sticky="w")
          
        searbtn=Button(F2,text="Search",width=10,command=self.search_da).grid(row=0,column=3,padx=10,pady=5)
        showalltn=Button(F2,text="ShowAll",width=10,command=self.fetch_da).grid(row=0,column=4,padx=10,pady=5)
        
        
        
        F4=Frame(F2,bd=4,relief=RIDGE,bg="dark slate grey")
        F4.place(x=10,y=55,width=760,height=400)   
        scroll_x=Scrollbar(F4,orient=HORIZONTAL)
        scroll_y=Scrollbar(F4,orient=VERTICAL)
            
        self.Admsn_table=ttk.Treeview(F4,columns=("AID","SNAME","CCODE","CNAME","Branch","DOA"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                    
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Admsn_table.xview)

            #table
        scroll_y.config(command=self.Admsn_table.yview)
        self.Admsn_table.heading("AID",text="ADMISSION ID")
        self.Admsn_table.heading("SNAME",text="Student Name")
        self.Admsn_table.heading("CCODE",text="Course Code")
        self.Admsn_table.heading("CNAME",text="Course Name")
        self.Admsn_table.heading("DOA",text="Date OF Admission")
        self.Admsn_table.heading("Branch",text="Branch")
        self.Admsn_table['show']="headings"
        self.Admsn_table.column("AID",width=100)
        self.Admsn_table.column("SNAME",width=100)
        self.Admsn_table.column("CCODE",width=100)
        self.Admsn_table.column("CNAME",width=100)
        self.Admsn_table.column("Branch",width=100)
        self.Admsn_table.column("DOA",width=100)
        self.Admsn_table.bind("<ButtonRelease-1>",self.get_foco)
        
            
        self.Admsn_table.pack(fill=BOTH,expand=1)
        self.fetch_da()


    def add_admsn(self):
        G=self.Adid_var.get()
        S=self.Sname_var.get()
        C=self.Ccode_var.get()
        Q=self.Cname_var.get()
        B=self.Branch_var.get()
        X=self.Doa_var.get()

        if G=='' or S=='' or C=='' or Q=='' or B=='' or X=='':
            messagebox.showerror("Error","All Fields Are Required!!!")
        else:

            con=cx_Oracle.connect("system/Prince")
            cur=con.cursor()
            cur.execute("INSERT INTO Admission(ADMISSIONID,NAME,COURSECODE,COURSENAME,BRANCH,DATEOFADMISSION)VALUES(:1,:2,:3,:4,:5,:6)", (G,S,C,Q,B,X))                                                               
            con.commit()
            self.fetch_da()
            messagebox.showinfo("Success","Record has been Added Successfull")
            #self.clear_da()
            con.close()
            

    def fetch_da(self):
            con=cx_Oracle.connect("system/Prince")
            cur=con.cursor()
            cur.execute("select * from Admission")
            rows = cur.fetchall()
            if (rows)!=0:
                self.Admsn_table.delete(*self.Admsn_table.get_children())
                for row in rows:
                    self.Admsn_table.insert('',END,values=row)
                con.commit()
            con.close()


    def clear_da(self):
            G=self.Adid_var.get()
            S=self.Sname_var.get()
            C=self.Ccode_var.get()
            Q=self.Cname_var.get()
            B=self.Branch_var.get()
            X=self.Doa_var.get()

            if (G=='' or S=='' or C=='' or Q=='' or B=='' or X==''):
                messagebox.showerror("Error","All Fields Are Required!!!")
            else:
                self.Adid_var.set('')
                self.Sname_var.set('')
                self.Ccode_var.set('')
                self.Cname_var.set('')
                self.Branch_var.set('')
                self.Doa_var.set('')
                messagebox.showinfo("Success","Record Cleared Successfully")

    def get_foco(self,event):
            cursor_row=self.Admsn_table.focus()
            contents=self.Admsn_table.item(cursor_row)
            row=contents['values']
            self.Adid_var.set(row[0])
            self.Sname_var.set(row[1])
            self.Ccode_var.set(row[2])
            self.Cname_var.set(row[3])
            self.Branch_var.set(row[4])
            self.Doa_var.set(row[5])


    def update_det(self):
        G=self.Adid_var.get()
        S=self.Sname_var.get()
        C=self.Ccode_var.get()
        Q=self.Cname_var.get()
        B=self.Branch_var.get()
        X=self.Doa_var.get()
        con=cx_Oracle.connect("system/Prince")
        cur=con.cursor()
        sql="UPDATE Admission SET NAME=:2,COURSECODE=:3,COURSENAME=:4,BRANCH=:5 where ADMISSIONID=:1"
        cur.execute(sql,(S,C,Q,B,G))
        con.commit()
        self.fetch_da()
        messagebox.showinfo("Success","Record Updated Successfully")
        self.clear_da()
        con.close()
        

    def delete_dat(self):
        con=cx_Oracle.connect("system/Prince")
        cur=con.cursor()
        cur.execute("Delete From  Admission where ADMISSIONID='%s'"%self.Adid_var.get())
        #rows = cur.fetchall()
        con.commit()
        con.close()
        self.fetch_da()
        self.clear_da()


    def search_da(self):
        con=cx_Oracle.connect("system/Prince")
        cur=con.cursor()
        
        cur.execute("select * from Admission where "+str(self.search_byy_var.get())+" LIKE '%"+str(self.search_txxt_var.get()+"%'"))
        rows = cur.fetchall()
        if (rows)!=0:
            self.Admsn_table.delete(*self.Admsn_table.get_children())
            for row in rows:
                self.Admsn_table.insert('',END,values=row)
            con.commit()
        con.close()

    
            



            
            


    
            
       
            
        
    
    
    
    
    
    
    
if __name__ == "__main__":
     window2=Tk()    
     ob=Admission(window2)
     window2.mainloop()
