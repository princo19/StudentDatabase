from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle
class Parent:
    def __init__(self,window):
            
            self.window=window
            self.window.title("Parents Details")
            self.window.geometry("1550x900")
        
        
            title=Label(self.window,text="Parents Detail",bd=10,relief=GROOVE,font=("times new roman",20,"bold"),bg="dark slate grey",fg="white")
            title.pack(side=TOP,fill=X)

            self.Roll1_no_var=StringVar()
            self.Fname_var=StringVar()
            self.Sname_var=StringVar()
            self.Fo_var=StringVar()
            self.Mname_var=StringVar()
            self.Mo_var=StringVar()
            self.mobile1_var=StringVar()
            self.email1_var=StringVar()
            self.search_buy_var=StringVar()
            self.search_text_var=StringVar()
                
            
            
           
            
            
            E1=Frame(window,bd=4,relief=RIDGE,bg="dark slate grey")
            E1.place(x=10,y=70,width=450,height=600)
                
            m1_title=Label(E1,text="Manage Parents",font=("times new roman",20,"bold"),bg="crimson",fg="white")
            m1_title.grid(row=0,column=0,pady=10)
                
            lbl_roll=Label(E1,text="Roll No",font=("times new roman",18,"bold"),bg="crimson",fg="white")
            lbl_roll.grid(row=1,column=0,pady=5,padx=5,sticky="w")
                
            txt_roll=Entry(E1,font=("times new roman",12,"bold"),textvariable=self.Roll1_no_var,relief=GROOVE,bd=5)
            txt_roll.grid(row=1,column=1,pady=5,padx=5,sticky="w")
            
            lbl_Sname=Label(E1,text="Name",font=("times new roman",18,"bold"),bg="crimson",fg="white")
            lbl_Sname.grid(row=2,column=0,pady=5,padx=5,sticky="w")
                
            txt_Sname=Entry(E1,textvariable=self.Sname_var,relief=GROOVE,bd=5,font=("times new roman",12,"bold"))
            txt_Sname.grid(row=2,column=1,pady=5,padx=5,sticky="w")
                
            lbl_Fname=Label(E1,text="Father Name",font=("times new roman",18,"bold"),bg="crimson",fg="white")
            lbl_Fname.grid(row=3,column=0,pady=5,padx=5,sticky="w")
                
            txt_Fname=Entry(E1,textvariable=self.Fname_var,relief=GROOVE,bd=5,font=("times new roman",12,"bold"))
            txt_Fname.grid(row=3,column=1,pady=5,padx=5,sticky="w")
                
            lbl_Mname=Label(E1,text="Mother Name",font=("times new roman",18,"bold"),bg="crimson",fg="white")
            lbl_Mname.grid(row=4,column=0,pady=5,padx=5,sticky="w")
                
            txt_Mname=Entry(E1,textvariable=self.Mname_var,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
            txt_Mname.grid(row=4,column=1,pady=5,padx=5,sticky="w")
                
                
            lbl_FO=Label(E1,text="Father Occupation",font=("times new roman",18,"bold"),bg="crimson",fg="white")
            lbl_FO.grid(row=5,column=0,pady=5,padx=5,sticky="w")
                
            txt_FO=Entry(E1,textvariable=self.Fo_var,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
            txt_FO.grid(row=5,column=1,pady=5,padx=5,sticky="w")
                
            lbl_MO=Label(E1,text="Mother Occupation",font=("times new roman",18,"bold"),bg="crimson",fg="white")
            lbl_MO.grid(row=6,column=0,pady=5,padx=5,sticky="w")
                
            txt_MO=Entry(E1,textvariable=self.Mo_var,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
            txt_MO.grid(row=6,column=1,pady=5,padx=5,sticky="w")
                
            lbl_EMAIL=Label(E1,text="Email",font=("times new roman",18,"bold"),bg="crimson",fg="white")
            lbl_EMAIL.grid(row=7,column=0,pady=5,padx=5,sticky="w")
                
            txt_EMAIL=Entry(E1,textvariable=self.email1_var,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
            txt_EMAIL.grid(row=7,column=1,pady=5,padx=5,sticky="w")
                
            lbl_phone=Label(E1,text="Mobile No",font=("times new roman",18,"bold"),bg="crimson",fg="white")
            lbl_phone.grid(row=8,column=0,pady=5,padx=5,sticky="w")
                
            txt_phone=Entry(E1,textvariable=self.mobile1_var,font=("times new roman",12,"bold"),relief=GROOVE,bd=5)
            txt_phone.grid(row=8,column=1,pady=5,padx=5,sticky="w")
            
            
            E3=Frame(E1,bd=4,relief=RIDGE,bg="black",padx=10)
            E3.place(x=15,y=450,width=420)
                
                
            Addbtn1=Button(E3,text="Add",width=10,command=self.add_parents).grid(row=0,column=0,padx=10,pady=5)
            Uptbtn1=Button(E3,text="Update",width=10,command=self.update_detai).grid(row=0,column=1,padx=10,pady=5)
            Delebtn1=Button(E3,text="Delete",width=10,command=self.delete_dat).grid(row=0,column=2,padx=10,pady=5)
            Cletn1=Button(E3,text="Clear",width=10,command=self.clear_data).grid(row=0,column=3,padx=10,pady=5)
            
            
            
            E2=Frame(window,bd=4,relief=RIDGE,bg="dark slate grey")
            E2.place(x=500,y=70,width=830,height=600)
                
            lbl_searc=Label(E2,text="Search By",font=("times new roman",18,"bold"),bg="crimson",fg="white")
            lbl_searc.grid(row=0,column=0,pady=10,padx=20,sticky="w")
                
            combo_searc=ttk.Combobox(E2,width=10,textvariable=self.search_buy_var,font=("times new roman",12,"bold"),state="readonly")
            combo_searc["value"]=("RollNo","Name")
            combo_searc.grid(row=0,column=1,padx=10,pady=10)
                
            txt_searc=Entry(E2,width=15,font=("times new roman",10,"bold"),textvariable=self.search_text_var,relief=GROOVE,bd=5)
            txt_searc.grid(row=0,column=2,pady=10,padx=20,sticky="w")
              
            searcbtn=Button(E2,text="Search",width=10,command=self.search_dat).grid(row=0,column=3,padx=10,pady=5)
            showallbtn=Button(E2,text="ShowAll",width=10,command=self.fetch_dat).grid(row=0,column=4,padx=10,pady=5)
            
            
            
            E4=Frame(E2,bd=4,relief=RIDGE,bg="dark slate grey")
            E4.place(x=10,y=55,width=760,height=400)   
            scroll_x=Scrollbar(E4,orient=HORIZONTAL)
            scroll_y=Scrollbar(E4,orient=VERTICAL)
                
            self.Parent_table=ttk.Treeview(E4,columns=("Roll","SName","FName","Mname","FOC","MOC","Email","Mobile"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                        
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.Parent_table.xview)

                #table
            scroll_y.config(command=self.Parent_table.yview)
            self.Parent_table.heading("Roll",text="Roll No.")
            self.Parent_table.heading("SName",text="Student Name")
            self.Parent_table.heading("FName",text="Father's Name")
            self.Parent_table.heading("Email",text="Email")
            self.Parent_table.heading("Mname",text="Mother's Name")
            #self.Student_table.heading("Address",text="Address")
            self.Parent_table.heading("FOC",text="F Occupation")
            self.Parent_table.heading("MOC",text="M Occupation")
            self.Parent_table.heading("Mobile",text="Mobile No.")
            self.Parent_table['show']="headings"
            self.Parent_table.column("Roll",width=100)
            self.Parent_table.column("FName",width=100)
            self.Parent_table.column("Mobile",width=100)
            #self.Student_table.column("Address",width=100)
            self.Parent_table.column("Mname",width=100)
            self.Parent_table.column("MOC",width=100)
            self.Parent_table.column("FOC",width=100)
            self.Parent_table.column("Email",width=100)
            self.Parent_table.bind("<ButtonRelease-1>",self.get_focus)
                
                
            self.Parent_table.pack(fill=BOTH,expand=1)
            self.fetch_dat()
            

            
    def add_parents(self):
            L=self.Roll1_no_var.get()
            S=self.Sname_var.get()
            F=self.Fname_var.get()
            M=self.Mname_var.get()
            O=self.Fo_var.get()
            T=self.Mo_var.get()
            W=self.email1_var.get()
            P=self.mobile1_var.get()
            if (L=="" or S=="" or F=="" or M=="" or O=="" or T=="" or W=="" or P=="") :
               messagebox.showerror("Error","All Fields Are Required!!!")
            else:
                
                con=cx_Oracle.connect("system/Prince")
                cur=con.cursor()
                cur.execute("INSERT INTO Parents(RollNo,Name,FatherName,MotherName,FatherOccupation,MotherOccupation,Email,MobileNo)VALUES(:1,:2,:3,:4,:5,:6,:7,:8)", (L,S,F,M,O,T,W,P))                                                               
                con.commit()
                self.fetch_dat()
                messagebox.showinfo("Success","Record has been Added Successfull")
                self.clear_data()
                con.close()
                

    def fetch_dat(self):
            con=cx_Oracle.connect("system/Prince")
            cur=con.cursor()
            cur.execute("select * from Parents")
            rows = cur.fetchall()
            if (rows)!=0:
                self.Parent_table.delete(*self.Parent_table.get_children())
                for row in rows:
                    self.Parent_table.insert('',END,values=row)
                con.commit()
            con.close()


    def clear_data(self):
            L=self.Roll1_no_var.get()
            S=self.Sname_var.get()
            F=self.Fname_var.get()
            M=self.Mname_var.get()
            O=self.Fo_var.get()
            T=self.Mo_var.get()
            W=self.email1_var.get()
            P=self.mobile1_var.get()
            if (L=="" or S=="" or F=="" or M=="" or O=="" or T=="" or W=="" or P=="") :
                messagebox.showerror("Error","All Fields Are Required!!!")
            else:
                self.Roll1_no_var.set('')
                self.Sname_var.set('')
                self.Fname_var.set('')
                self.Mname_var.set('')
                self.Fo_var.set('')
                self.Mo_var.set('')
                self.email1_var.set('')
                self.mobile1_var.set('')
                messagebox.showinfo("Success","Record Cleared Successfully")



    def get_focus(self,events):
        cursor_row=self.Parent_table.focus()
        contents=self.Parent_table.item(cursor_row)
        row=contents['values']
        self.Roll1_no_var.set(row[0])
        self.Sname_var.set(row[1])
        self.Fname_var.set(row[2])
        self.Mname_var.set(row[3])
        self.Fo_var.set(row[4])
        self.Mo_var.set(row[5])
        self.email1_var.set(row[6])
        self.mobile1_var.set(row[7])


    def update_detai(self):
        L=self.Roll1_no_var.get()
        S=self.Sname_var.get()
        F=self.Fname_var.get()
        M=self.Mname_var.get()
        O=self.Fo_var.get()
        T=self.Mo_var.get()
        W=self.email1_var.get()
        P=self.mobile1_var.get()
        con=cx_Oracle.connect("system/Prince")
        cur=con.cursor()
        sql="UPDATE Parents SET Name=:2,FatherName=:3,MotherName=:4,FatherOccupation=:5,MotherOccupation=:6,Email=:7,MobileNo=:8 where RollNo=:1"
        cur.execute(sql,(S,F,M,O,T,W,P,L))
        con.commit()
        self.fetch_dat()
        messagebox.showinfo("Success","Record Updated Successfully")
        self.clear_data()
        con.close()

        


    def delete_dat(self):
        con=cx_Oracle.connect("system/Prince")
        cur=con.cursor()
        cur.execute("Delete From  Parents where RollNo='%s'"%self.Roll1_no_var.get())
        #rows = cur.fetchall()
        con.commit()
        con.close()
        self.fetch_dat()
        self.clear_data()

    def search_dat(self):
        con=cx_Oracle.connect("system/Prince")
        cur=con.cursor()
        
        cur.execute("select * from Parents where "+str(self.search_buy_var.get())+" LIKE '%"+str(self.search_text_var.get()+"%'"))
        rows = cur.fetchall()
        if (rows)!=0:
            self.Parent_table.delete(*self.Parent_table.get_children())
            for row in rows:
                self.Parent_table.insert('',END,values=row)
            con.commit()
        con.close()


    
        
               
    

if __name__ == "__main__":
    window=Tk()
    ob=Parent(window)
    window.mainloop()

             
