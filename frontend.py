# front end
from tkinter import *
import tkinter.messagebox
import backend as pb


class employee:

    def __init__(self, root):
        self.root = root
        self.root.title("Employee Database Management System")
        self.root.geometry(newGeometry="1328x585+0+0")
        self.root.config(bg="blue")
        # ASSIGN SOME VARIABLE TO STORE OUR ENTRY FILELD VALUES

        empId = StringVar()
        name = StringVar()
        salary = StringVar()
        dept = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()
        ################FUNCTIONS
        pb.empData()

        def iExit():
            iExit = tkinter.messagebox.askyesno("Mgm's employee dbms", "confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return

        def clearData():
            self.txtempId.delete(0, END)
            self.txtname.delete(0, END)
            self.txtsalary.delete(0, END)
            self.txtdept.delete(0, END)
            self.txtAge.delete(0, END)
            self.txtGender.delete(0, END)
            self.txtAdress.delete(0, END)
            self.txtMobile.delete(0, END)

        pb.empData()

        def addData():
            if (len(empId.get()) != 0):
                pb.addempRec(empId.get(), name.get(), salary.get(), dept.get(), Age.get(), Gender.get(),
                             Address.get(), Mobile.get())
                emplist.delete(0, END)
                emplist.insert(END, (
                empId.get(), name.get(), salary.get(), dept.get(), Age.get(), Gender.get(), Address.get(),
                Mobile.get()))

        def DisplayData():
            emplist.delete(0, END)
            for row in pb.viewData():
                emplist.insert(END, row)

        def empRec(event):
            global sd
            searchemp = emplist.curselection()[0]
            sd = emplist.get(searchemp)
            self.txtempId.delete(0, END)
            self.txtempId.insert(END, sd[0])
            self.txtname.delete(0, END)
            self.txtname.insert(END, sd[1])
            self.txtsalary.delete(0, END)
            self.txtsalary.insert(END, sd[2])
            self.txtdept.delete(0, END)
            self.txtdept.insert(END, sd[3])
            self.txtAge.delete(0, END)
            self.txtAge.insert(END, sd[4])
            self.txtGender.delete(0, END)
            self.txtGender.insert(END, sd[5])
            self.txtAdress.delete(0, END)
            self.txtAdress.insert(END, sd[6])
            self.txtMobile.delete(0, END)
            self.txtMobile.insert(END, sd[7])

        def DeleteData():

            if (len(empId.get()) != 0):
                pb.deleteRec(sd[0])
                clearData()
                DisplayData()

        def searchDatabase():
            emplist.delete(0, END)
            for row in pb.searchData(empId.get(), name.get(), salary.get(), dept.get(), Age.get(), Gender.get(),
                                     Address.get(), Mobile.get()):
                emplist.insert(END, row, str(""))

        def update():
            if (len(empId.get()) != 0):
                pb.deleteRec(sd[0])
            if (len(empId.get()) != 0):
                pb.addempRec(empId.get(), name.get(), salary.get(), dept.get(), Age.get(), Gender.get(),
                             Address.get(), Mobile.get())
                emplist.delete(0, END)
                emplist.insert(END, (
                empId.get(), name.get(), salary.get(), dept.get(), Age.get(), Gender.get(), Address.get(),
                Mobile.get()))

                #################################FRAMES

        MainFrame = Frame(self.root, bg="white")
        MainFrame.grid()  # THIS IS MAIN FRAME FOR OUR WINDOW
        TitFrame = Frame(MainFrame, bd=1, padx=54, pady=8, bg="blue", relief=RIDGE)
        TitFrame.pack(side=TOP)  # THIS IS THE TITLE FRAME

        self.lblTit = Label(TitFrame, font=('arial', 47, 'bold'), text="Employee Database Management System", bg="blue",
                            fg="white")
        self.lblTit.grid()

        self.lblTit = Label(TitFrame, font=('arial', 25, 'bold'), text="MGM COLLEGE OF ENGINEERING AND PHARMACEUTICAL SCIENCES", bg="blue", fg="black")
        self.lblTit.grid()

        self.lblTit = Label(TitFrame, font=('arial', 12), text="Valanchery, Malappuram, Kerala", bg="blue", fg="green")
        self.lblTit.grid()

        ButtonFrame = Frame(MainFrame, bd=1, width=1350, height=70, padx=18, pady=10, bg="green", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)  #

        DataFrame = Frame(MainFrame, bd=9, width=1300, height=400, padx=20, pady=20, bg="#CDCDC0", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)  # THIS IS STI

        DataFrameLeft = LabelFrame(DataFrame, font=('arial', 12, 'bold'), bd=1, width=450, height=300, bg="Ghost White",
                                   relief=RIDGE, text="Enter Employee Information:\n")
        DataFrameLeft.pack(side=LEFT)

        DataFrameRight = LabelFrame(DataFrame, font=('arial', 12, 'bold'), bd=1, width=450, height=300,
                                    bg="Ghost White", relief=RIDGE, text="Employee Details\n")
        DataFrameRight.pack(side=RIGHT)
        #########################################Lables and entry widget

        self.lblempId = Label(DataFrameLeft, font=('arial', 12, 'bold'), padx=2, pady=3, text="Employee Id:",
                              bg="ghost white")
        self.lblempId.grid(row=0, column=0, sticky=W)

        self.txtempId = Entry(DataFrameLeft, font=('arial', 12, 'bold'), textvariable=empId, bg="ghost white", width=39)
        self.txtempId.grid(row=0, column=1)  # emp id

        self.lblname = Label(DataFrameLeft, font=('arial', 12, 'bold'), padx=2, pady=3, text="Name:",
                                  bg="ghost white")
        self.lblname.grid(row=1, column=0, sticky=W)

        self.txtname = Entry(DataFrameLeft, font=('arial', 12, 'bold'), textvariable=name, bg="ghost white",
                                  width=39)
        self.txtname.grid(row=1, column=1)  # name

        self.lblsalary = Label(DataFrameLeft, font=('arial', 12, 'bold'), padx=2, pady=3, text="Salary:",
                                bg="ghost white")
        self.lblsalary.grid(row=2, column=0, sticky=W)

        self.txtsalary = Entry(DataFrameLeft, font=('arial', 12, 'bold'), textvariable=salary, bg="ghost white",
                                width=39)
        self.txtsalary.grid(row=2, column=1)  # last name

        self.lbldept = Label(DataFrameLeft, font=('arial', 12, 'bold'), padx=2, pady=3, text="Department",
                            bg="ghost white")
        self.lbldept.grid(row=3, column=0, sticky=W)

        self.txtdept = Entry(DataFrameLeft, font=('arial', 12, 'bold'), textvariable=dept, bg="ghost white", width=39)
        self.txtdept.grid(row=3, column=1)  # dept

        self.lblAge = Label(DataFrameLeft, font=('arial', 12, 'bold'), padx=2, pady=3, text="Age:", bg="ghost white")
        self.lblAge.grid(row=4, column=0, sticky=W)

        self.txtAge = Entry(DataFrameLeft, font=('arial', 12, 'bold'), textvariable=Age, bg="ghost white", width=39)
        self.txtAge.grid(row=4, column=1)  # age

        self.lblGender = Label(DataFrameLeft, font=('arial', 12, 'bold'), padx=2, pady=3, text="Gender:",
                               bg="ghost white")
        self.lblGender.grid(row=5, column=0, sticky=W)

        self.txtGender = Entry(DataFrameLeft, font=('arial', 12, 'bold'), textvariable=Gender, bg="ghost white",
                               width=39)
        self.txtGender.grid(row=5, column=1)  # gender

        self.lblAdress = Label(DataFrameLeft, font=('arial', 12, 'bold'), padx=2, pady=3, text="Address:",
                               bg="ghost white")
        self.lblAdress.grid(row=6, column=0, sticky=W)

        self.txtAdress = Entry(DataFrameLeft, font=('arial', 12, 'bold'), textvariable=Address, bg="ghost white",
                               width=39)
        self.txtAdress.grid(row=6, column=1)  # adress

        self.lblMobile = Label(DataFrameLeft, font=('arial', 12, 'bold'), padx=2, pady=3, text="Mobile Number:",
                               bg="ghost white")
        self.lblMobile.grid(row=7, column=0, sticky=W)

        self.txtMobile = Entry(DataFrameLeft, font=('arial', 12, 'bold'), textvariable=Mobile, bg="ghost white",
                               width=39)
        self.txtMobile.grid(row=7, column=1)  # mobile

        ###############################List Box and ScrollBar Widget
        scrollbar = Scrollbar(DataFrameRight)
        scrollbar.grid(row=0, column=1, sticky='ns')  # scroll bar

        emplist = Listbox(DataFrameRight, width=68, height=12, font=('arial', 12, 'bold'),
                              yscrollcommand=scrollbar.set)
        emplist.bind('<<ListboxSelect>>', empRec)
        emplist.grid(row=0, column=0, padx=10)
        scrollbar.config(command=emplist.yview)

        ##################################Button Widget
        self.btnAddData = Button(ButtonFrame, text="Add New", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                 fg="#555", command=addData)
        self.btnAddData.grid(row=0, column=0)  # ADD NEW

        self.btnDisplay = Button(ButtonFrame, text="Display", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                 fg="#555", command=DisplayData)
        self.btnDisplay.grid(row=0, column=1)  # DISPLAY

        self.btnClear = Button(ButtonFrame, text="Clear", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                               fg="#555", command=clearData)
        self.btnClear.grid(row=0, column=2)  # CLEAR

        self.btnDelete = Button(ButtonFrame, text="Delete", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                fg="#555", command=DeleteData)
        self.btnDelete.grid(row=0, column=3)  # DELETE

        self.btnSearch = Button(ButtonFrame, text="Search", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                fg="#555", command=searchDatabase)
        self.btnSearch.grid(row=0, column=4)  # SEARCH

        self.btnUpdate = Button(ButtonFrame, text="Update", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                fg="#555", command=update)
        self.btnUpdate.grid(row=0, column=5)  # UPDATE

        self.btnExit = Button(ButtonFrame, text="Exit", font=('arial', 20, 'bold'), height=1, width=10, bd=4, fg="#555",
                              command=iExit)
        self.btnExit.grid(row=0, column=6)  # EXIT


if __name__ == '__main__':
    root = Tk()  # CREATE AN OBJECT
    application = employee(root)  # PASS IT TO OUR CLASS WHITH ITS PROPERTIES IN CLASS
    root.mainloop()  # RUN UNTIL CLOSING THE WINDOW MANUALLY