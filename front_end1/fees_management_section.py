from tkinter import*
from tkinter import ttk
from back_end1.register_connection import*
from tkinter import messagebox
from model_class1.fee_model import*
class Fees:
    def __init__(self,screen):
        self.wn=screen
        self.wn.geometry("1480x830+50+0")
        self.wn.title("Fees management".center(480))
        self.wn.config(background="#003333")
        self.con_fee=register_database()
        # #self.wn.focus_set()
        # #self.wn.focus_force()
        # self.wn.focus_set()
        # ======first frame=========
        self.fcontainer = Frame(self.wn, bg="#996633", bd=10, relief=RIDGE)
        self.fcontainer.place(x=10, y=10, width=600, height=820)
        self.head2 = Label(self.fcontainer, text=" Student Fees Details", font=("times new roman", 25, "bold"),
                           bg="#996633",fg="black")
        self.head2.pack(side=TOP)
        # =====heading=======
        self.head1 = Label(self.wn, text="STUDENT  FEES", font=("times new roman", 30, "bold"), bg="#003333",
                           fg="red")
        self.head1.place(x=700, y=0)
        #=======second container========
        self.scontainer=Frame(self.wn, bg="#996633", bd=10, relief=RIDGE)
        self.scontainer.place(x=620,y=50,width=850,height=780)
        #=====third frame========
        self.tcontainer=Frame(self.scontainer,bg="light blue",bd=2,relief=GROOVE)
        self.tcontainer.place(x=0,y=0,width=827,height=50)

        #====button for viewing all data=========
        self.view_btn=Button(self.tcontainer,text="View All Data",font=("arial",15,"bold"),bd=5,bg="light green",command=self.view_window)
        self.view_btn.place(x=300,y=3,width=200,height=40)

        #====searching========
        lbl_search = Label(self.scontainer, text="Search By:", font=("times new roman", 25, "bold"), fg="yellow",
                           bg="#996633")
        lbl_search.place(x=10,y=50)
        self.combo_search1 = ttk.Combobox(self.scontainer, width=13,
                                    font=("times new roman", 13, "bold"), state="readonly")
        self.combo_search1["values"] = ("ID_No")
        self.combo_search1.place(x=200,y=60,width=200)
        self.search_ent1 = Entry(self.scontainer, font=("arial", 12, "bold"), bd=1, relief=GROOVE)
        self.search_ent1.place(x=450,y=60,width=200)
        search_btn = Button(self.scontainer, text="Search", font=("times new roman", 15, "bold"), bd=5, fg="black",
                            bg="white",
                            width=8,command=self.search_data)
        search_btn.place(x=700,y=60)

        #======fourth container======
        self.fourthcontainer = Frame(self.scontainer, bg="white", bd=5, relief=RIDGE)
        self.fourthcontainer.place(x=10, y=110, width=810, height=640)
        #====student id==========
        self.id = Label(self.fcontainer, text="Student_ID_No:", font=("times new roman", 20, "bold"),
                        fg="yellow", bg="#996633")
        self.id.place(x=10, y=70)
        self.ent_id = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                              relief=GROOVE, bg="lightgray")
        self.ent_id.place(x=260, y=75)
        #======first name======
        self.firstname = Label(self.fcontainer, text="First_Name:", font=("times new roman", 20, "bold"),
                        fg="yellow", bg="#996633")
        self.firstname.place(x=10, y=140)
        self.ent_Name = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                              relief=GROOVE, bg="lightgray")
        self.ent_Name.place(x=260, y=145)
        #===last name======
        self.lastname = Label(self.fcontainer, text="Last_Name:", font=("times new roman", 20, "bold"),
                               fg="yellow", bg="#996633")
        self.lastname.place(x=10, y=210)
        self.ent_lname = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                              relief=GROOVE, bg="lightgray")
        self.ent_lname.place(x=260, y=215)
        #====total fees=========
        self.fee = Label(self.fcontainer, text="Total Fees:", font=("times new roman", 20, "bold"),
                              fg="yellow", bg="#996633")
        self.fee.place(x=10, y=280)
        self.ent_fee = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                              relief=GROOVE, bg="lightgray")
        self.ent_fee.place(x=260, y=285)
        #======semester=====
        self.semester = Label(self.fcontainer, text="Semester:", font=("times new roman", 20, "bold"),
                              fg="yellow", bg="#996633")
        self.semester.place(x=10, y=350)
        self.sem = ttk.Combobox(self.fcontainer, font=("times new roman", 12, "bold"))
        self.sem["values"] = ("1st", "2nd","3rd","4th","5th","6th","7th","8th")
        self.sem.place(x=260, y=355, width=190)
        #====year======
        self.year = Label(self.fcontainer, text="Year:", font=("times new roman", 20, "bold"),
                              fg="yellow", bg="#996633")
        self.year.place(x=10, y=420)
        self.yr = ttk.Combobox(self.fcontainer, font=("times new roman", 12, "bold"))
        self.yr["values"] = ("1st year", "2nd year", "3rd year", "4th year")
        self.yr.place(x=260, y=425, width=190)
        #=======paid amount===
        self.paid = Label(self.fcontainer, text="Paid_Amount:", font=("times new roman", 20, "bold"),
                          fg="yellow", bg="#996633")
        self.paid.place(x=10, y=490)
        self.ent_paid = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                              relief=GROOVE, bg="lightgray")
        self.ent_paid.place(x=260, y=495)