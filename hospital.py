from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital management system")
        self.root.geometry("150x800+0+0")

        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.sideEfect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()


        lbltitle=Label(self.root,bd=9,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM ",fg="#2E86C1",bg="white",font=("Helvetica", 50, "italic"))
        lbltitle.pack(side=TOP,fill=X)

        #======== DATA FRRAME==================
        DataFrame=Frame(self.root,bd=9,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1530,height=390)

        DataFrameLeft=LabelFrame(DataFrame,bd=9,relief=RIDGE,padx=10,font=("Helvetica",12,"italic"),text="Patient Information")
        DataFrameLeft.place(x=0,y=5,width=980,height=350)

        DataFrameRight=LabelFrame(DataFrame,bd=9,relief=RIDGE,padx=10,font=("Helvetica",12,"italic"),text="Prescription")
        DataFrameRight.place(x=990,y=5,width=480,height=350)

        #==========Button=================

        Buttonframe=Frame(self.root,bd=9,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1520,height=60) 

        #==========Details Frame=================

        Detailsframe=Frame(self.root,bd=9,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)

         #==============DataFrameLeft=============

        lblNameTablet=Label(DataFrameLeft,text="Name of Tablet:",font=("arial",12,"italic"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)

        comNametablet=ttk.Combobox(DataFrameLeft,textvariable=self.Nameoftablets,state="readonly",font=("times new roman",12,"italic"),width=33)

        comNametablet["values"]=("Nice","Corona Vacacine","Adderall","Amlodipine","AAtivan")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)

        lblref=Label(DataFrameLeft,font=("arial",12,"italic"),text="Reference No:" ,padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLeft,font=("arial",13,"italic"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)

        lblDose=Label(DataFrameLeft,font=("arial",12,"italic"),text="Dose:" ,padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataFrameLeft,font=("arial",13,"italic"),textvariable=self.Dose,width=35)
        txtDose.grid(row=2,column=1)

        lblNoOftablets=Label(DataFrameLeft,font=("arial",12,"italic"),text="No Of Tablets:" ,padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtDose=Entry(DataFrameLeft,font=("arial",13,"italic"),textvariable=self.NumberofTablets,width=35)
        txtDose.grid(row=3,column=1)

        lblLot=Label(DataFrameLeft,font=("arial",12,"italic"),text="Lot:" ,padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataFrameLeft,font=("arial",13,"italic"),textvariable=self.Lot,width=35)
        txtLot.grid(row=4,column=1)

        lblissueDate=Label(DataFrameLeft,font=("arial",12,"italic"),text="Issue Date:" ,padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtissueDate=Entry(DataFrameLeft,font=("arial",13,"italic"),textvariable=self.Issuedate,width=35)
        txtissueDate.grid(row=5,column=1)

        lblExpDate=Label(DataFrameLeft,font=("arial",12,"italic"),text="Exp Date:" ,padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataFrameLeft,font=("arial",13,"italic"),textvariable=self.ExpDate,width=35)
        txtExpDate.grid(row=6,column=1)

        lblDailyDose=Label(DataFrameLeft,font=("arial",12,"italic"),text="Daily Dose:" ,padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataFrameLeft,font=("arial",13,"italic"),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)

        lblSideEffects=Label(DataFrameLeft,font=("arial",12,"italic"),text="Side Effects:" ,padx=2,pady=6)
        lblSideEffects.grid(row=8,column=0,sticky=W)
        txtSideEffects=Entry(DataFrameLeft,font=("arial",13,"italic"),textvariable=self.sideEfect,width=35)
        txtSideEffects.grid(row=8,column=1)

        lblFurtherInfo=Label(DataFrameLeft,font=("arial",12,"italic"),text="Further Info:" ,padx=2,pady=6)
        lblFurtherInfo.grid(row=0,column=2,sticky=W)
        txtFurtherInfo=Entry(DataFrameLeft,font=("arial",13,"italic"),textvariable=self.FurtherInformation,width=35)
        txtFurtherInfo.grid(row=0,column=3)

        lblBloodPressure=Label(DataFrameLeft,font=("arial",12,"italic"),text="Blood Pressure:" ,padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataFrameLeft,font=("arial",13,"italic"),textvariable=self.DrivingUsingMachine,width=35)
        txtBloodPressure.grid(row=1,column=3)

        lblStorage=Label(DataFrameLeft,font=("arial",12,"italic"),text="Storage Advice:" ,padx=2,pady=6)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataFrameLeft,font=("arial",13,"italic"),textvariable=self.StorageAdvice,width=35)
        txtStorage.grid(row=2,column=3)

        lblMedicine=Label(DataFrameLeft,font=("arial",12,"italic"),text="Medication" ,padx=2,pady=6)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataFrameLeft,font=("arial",13,"italic"),textvariable=self.HowToUseMedication,width=35)
        txtMedicine.grid(row=3,column=3)

        lblPatientId=Label(DataFrameLeft,font=("arial",12,"italic"),text="Patient Id" ,padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataFrameLeft,font=("arial",13,"italic"),textvariable=self.PatientId,width=35)
        txtPatientId.grid(row=4,column=3)

        lblNhsNumber=Label(DataFrameLeft,font=("arial",12,"italic"),text="NHS Number" ,padx=2,pady=6)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataFrameLeft,font=("arial",13,"italic"),textvariable=self.nhsNumber,width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientname=Label(DataFrameLeft,font=("arial",12,"italic"),text="Patient Name" ,padx=2,pady=6)
        lblPatientname.grid(row=6,column=2,sticky=W)
        txtPatientname=Entry(DataFrameLeft,font=("arial",13,"italic"),textvariable=self.PatientName,width=35)
        txtPatientname.grid(row=6,column=3)

        lblDateOfBirth=Label(DataFrameLeft,font=("arial",12,"italic"),text="Date Of Birth" ,padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(DataFrameLeft,font=("arial",13,"italic"),textvariable=self.DateOfBirth,width=35)
        txtDateOfBirth.grid(row=7,column=3)

        lblAddrss=Label(DataFrameLeft,font=("arial",12,"italic"),text="Patient Address" ,padx=2,pady=6)
        lblAddrss.grid(row=8,column=2,sticky=W)
        txtAddress=Entry(DataFrameLeft,font=("arial",13,"italic"),textvariable=self.PatientAddress,width=35)
        txtAddress.grid(row=8,column=3)

        self.txtPrescription=Text(DataFrameRight,font=("arial",12,"italic"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)


        #==============Buttons===============
        btnPrescription=Button(Buttonframe,bg="green",command=self.iPrectioption,fg="white",font=("arial",10,"bold"),text="Prescription",width=23,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)

        #buttonprescription = Button(Buttonframe,command=self.iPrectioption,text="Prescription",fg="White",bg="Orange",font=("arial",16,"bold"),width=23,padx=2,pady=6)
        #buttonprescription.grid(row=0,column=0)

        btnPrescriptionData=Button(Buttonframe,command=self.iPreescriptionData,bg="green",fg="white",font=("arial",10,"bold"),text="Prescription Data",width=23,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,bg="green",command=self.update_data,fg="white",font=("arial",10,"bold"),text="Update",width=23,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,command=self.idelete,bg="green",fg="white",font=("arial",10,"bold"),text="Delete",width=23,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,command=self.clear,bg="green",fg="white",font=("arial",10,"bold"),text="Clear",width=23,padx=2,pady=6)
        btnClear.grid(row=0,column=4)


        btnExit = Button(Buttonframe,command=self.iExit, bg="green", fg="white", font=("arial", 10,"bold"), text="Exit",width=23, padx=2, pady=6)
        btnExit.grid(row=0, column=5,sticky="ew")


        #=============Table=========
        #================Scrollabar===========
        scrol_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scrol_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftable","ref","dose","nooftablets","lot","issuedate",
                                "expdate","dailydose","storage","pId","nhsnumber","pname","dob","address"),xscrollcommand=scrol_x.set,yscrollcommand=scrol_y.set)
        scrol_x.pack(side=BOTTOM,fill=X)
        scrol_y.pack(side=RIGHT,fill=Y)

        scrol_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scrol_y=ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable",text="Name of Tablets")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No Of Tablets")
        self.hospital_table.heading("lot",text="Lots")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="NDaily Dose")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("pId",text="Patien Id")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"
        

        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("pId",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()



    #=========Functionality description===========
    def iPreescriptionData(self):
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            messagebox.showerror("Error","all flieds are required")
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="josvita",database="mydata")
            my_cursor=conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                    self.Nameoftablets.get(),
                                                    self.ref.get(),
                                                    self.Dose.get(),
                                                    self.NumberofTablets.get(),
                                                    self.Lot.get(),
                                                    self.Issuedate.get(),
                                                    self.DailyDose.get(),
                                                    self.StorageAdvice.get(),
                                                    self.nhsNumber.get(),
                                                    self.PatientName.get(),
                                                    self.DateOfBirth.get(),
                                                    self.PatientAddress.get()
                                                    ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")


    def update_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="josvita",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("update hospital set Nameoftablets=%s,Dose=%s,No_of_Tablets=%s,Lot=%s,Issue_Date=%s,Exp_Date=%s,Daily_Dose=%s,Storage=%s,NHSNumber=%s,Patient_Name=%s,DOB=%s,Address=%s where Reference_No=%s",
                                                (
                                                    self.Nameoftablets.get(),
                                                    self.Dose.get(),
                                                    self.NumberofTablets.get(),
                                                    self.Lot.get(),
                                                    self.Issuedate.get(),
                                                    self.Expdate.get(),
                                                    self.DailyDose.get(),
                                                    self.StorageAdvice.get(),
                                                    self.nhsNumber.get(),
                                                    self.PatientName.get(),
                                                    self.DateOfBirth.get(),
                                                    self.PatientAddress.get(),
                                                    self.ref.get(),
        
                                                    ))


        
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="josvita",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_childern())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_rows=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_rows)
        row=content["values"]
        self.Nameoftablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.StorageAdvice.set(row[8])
        self.nhsNumber.set(row[9])
        self.PatientName.set(row[10])
        self.DateOfBirth.set(row[11])
        self.PatientAddress.set(row[12])


    def iPrectioption(self):
        self.txtPrescription.insert(END,"name of Tablets:\t\t\t"+self.Nameoftablets.get()+"\n")
        self.txtPrescription.insert(END,"Reference No\t\t\t"+self.ref.get()+"\n")
        self.txtPrescription.insert(END,"Dose:\t\t\t"+self.Dose.get()+"\n")
        self.txtPrescription.insert(END,"Number of Tablets:\t\t\t"+self.NumberofTablets.get()+"\n")
        self.txtPrescription.insert(END,"Lot:\t\t\t"+self.Lot.get()+"\n")
        self.txtPrescription.insert(END,"Issue Date:\t\t\t"+self.Issuedate.get()+"\n")
        self.txtPrescription.insert(END,"Exp Date:\t\t\t"+self.Expdate.get()+"\n")
        self.txtPrescription.insert(END,"Daily Dose:\t\t\t"+self.DailyDose.get()+"\n")
        self.txtPrescription.insert(END,"Side Effect:\t\t\t"+self.sideEfect.get()+"\n")
        self.txtPrescription.insert(END,"Further Information:\t\t\t"+self.FurtherInformation.get()+"\n")
        self.txtPrescription.insert(END,"Storage Advice:\t\t\t"+self.StorageAdvice.get()+"\n")
        self.txtPrescription.insert(END,"DrivingUsingMachine:\t\t\t"+self.DrivingUsingMachine.get()+"\n")
        self.txtPrescription.insert(END,"Patient Id:\t\t\t"+self.PatientId.get()+"\n")
        self.txtPrescription.insert(END,"NHSNumber:\t\t\t"+self.nhsNumber.get()+"\n")
        self.txtPrescription.insert(END,"DateofBirth:\t\t\t"+self.DateofBirth.get()+"\n")
        self.txtPrescription.insert(END,"Patient Address:\t\t\t"+self.PatientAddress.get()+"\n")
     

    def idelete(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="josvita",database="mydata")
        my_cursor=conn.cursor()
        querry="delete from hospital where Reference_No=%s"
        value=(self.ref.get(),)
        my_cursor.execute(querry,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Delete","Patient has been deleted successfully")


    def clear(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEfect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.DrivingUsingMachine.set("")
        self.HowToUseMedication.set("")
        self.PatientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0",END)


    def iExit(self):
        iExit=messagebox.askyesno("Hospital management system","Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return


    
        





root=Tk()
ob=Hospital(root)
root.mainloop()