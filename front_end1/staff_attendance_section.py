from tkinter import*
from tkinter import ttk
from back_end1.register_connection import *
from tkinter import messagebox
from model_class1.staffattendance_model import*
from tkcalendar import*
class Staff_attendance:
    def __init__(self,screen):
        self.wn=screen
        self.wn.geometry("1480x830+50+0")
        self.wn.title("Staff attendance".center(480))
        self.wn.config(background="#333300")
        self.con_staffattendance=register_database()
        self.from_date_var = StringVar()
        self.to_date_var = StringVar()
        # ======first frame=========
        self.fcontainer = Frame(self.wn, bg="#669966", bd=10, relief=RIDGE)
        self.fcontainer.place(x=10, y=50, width=600, height=780)
        self.head2 = Label(self.fcontainer, text=" Attendance Details", font=("times new roman", 25, "bold"),
                           bg="#669966", fg="black")
        self.head2.pack(side=TOP)
        # =====heading=======
        self.head1 = Label(self.wn, text="STAFF   ATTENDANCE", font=("times new roman", 30, "bold"), bg="#333300",
                           fg="yellow")
        self.head1.place(x=700, y=0)
        # =======second container========
        self.scontainer = Frame(self.wn, bg="#669966", bd=10, relief=RIDGE)
        self.scontainer.place(x=620, y=50, width=850, height=780)
        # =====third frame========
        self.tcontainer = Frame(self.scontainer, bg="light blue", bd=2, relief=GROOVE)
        self.tcontainer.place(x=0, y=0, width=827, height=50)

        # ====button for viewing all data=========
        self.view_btn = Button(self.tcontainer, text="View All Data", font=("arial", 15, "bold"), bd=5,
                               bg="yellow", command=self.view_window)
        self.view_btn.place(x=600, y=3, width=200, height=40)
        # =====calender button===
        self.calender_btn = Button(self.tcontainer, text="Calender", font=("arial", 15, "bold"), bd=10,
                                   bg="black", fg="white", command=self.calc1)
        self.calender_btn.place(x=30, y=3, width=160, height=40)
        # =====get value1=====
        self.getvalue1_btn = Button(self.tcontainer, text="Get from-date", font=("arial", 15, "bold"), bd=10,
                                    bg="black", fg="white", command=self.getvalue1)
        self.getvalue1_btn.place(x=220, y=3, width=160, height=40)
        # ====get value2======
        self.getvalue2_btn = Button(self.tcontainer, text="Get to-date", font=("arial", 15, "bold"), bd=10,
                                    bg="black", fg="white", command=self.getvalue2)
        self.getvalue2_btn.place(x=410, y=3, width=160, height=40)

        #=====searching=====
        lbl_search = Label(self.scontainer, text="Search By:", font=("times new roman", 25, "bold"), fg="black",
                           bg="#669966")
        lbl_search.place(x=10, y=50)
        self.combo_search1 = ttk.Combobox(self.scontainer, width=13,
                                    font=("times new roman", 13, "bold"), state="readonly")
        self.combo_search1["values"] = ("ID_No")
        self.combo_search1.place(x=200, y=60, width=200)
        self.search_ent1 = Entry(self.scontainer, font=("arial", 12, "bold"), bd=1, relief=GROOVE)
        self.search_ent1.place(x=450, y=60, width=200)
        search_btn = Button(self.scontainer, text="Search", font=("times new roman", 15, "bold"), bd=5, fg="black",
                            bg="white",
                            width=8,command=self.search_data)
        search_btn.place(x=700, y=60)

        # ======fourth container======
        self.fourthcontainer = Frame(self.scontainer, bg="white", bd=5, relief=RIDGE)
        self.fourthcontainer.place(x=10, y=110, width=810, height=640)
        # ====student id==========
        self.firstname = Label(self.fcontainer, text="First_Name:", font=("times new roman", 20, "bold"),
                        fg="black", bg="#669966")
        self.firstname.place(x=10, y=70)
        self.ent_Name = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                            relief=GROOVE, bg="lightgray")
        self.ent_Name.place(x=300, y=75)
        # ======first name======
        self.lastname = Label(self.fcontainer, text="Last_Name:", font=("times new roman", 20, "bold"),
                               fg="black", bg="#669966")
        self.lastname.place(x=10, y=140)
        self.ent_lname = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                              relief=GROOVE, bg="lightgray")
        self.ent_lname.place(x=300, y=145)
        # ===last name======
        self.staffid = Label(self.fcontainer, text="Staff_ID_No:", font=("times new roman", 20, "bold"),
                              fg="black", bg="#669966")
        self.staffid.place(x=10, y=210)
        self.ent_id = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                               relief=GROOVE, bg="lightgray")
        self.ent_id.place(x=300, y=215)
        # ====from=========
        self.from_date = Label(self.fcontainer, text="From:", font=("times new roman", 20, "bold"),
                               fg="black", bg="#669966")
        self.from_date.place(x=10, y=280)
        self.ent_fromdate = Entry(self.fcontainer, textvariable=self.from_date_var, font=("arial", 12, "bold"), bd=1,
                                  relief=GROOVE, bg="lightgray")
        self.ent_fromdate.place(x=300, y=285)
        # ======to=====
        self.to = Label(self.fcontainer, text="To:", font=("times new roman", 20, "bold"),
                        fg="black", bg="#669966")
        self.to.place(x=10, y=350)
        self.ent_todate = Entry(self.fcontainer,textvariable=self.to_date_var, font=("arial", 12, "bold"), bd=1,
                               relief=GROOVE, bg="lightgray")
        self.ent_todate.place(x=300, y=355)
        # ====total days======
        self.total_days = Label(self.fcontainer, text="Total number of days:", font=("times new roman", 20, "bold"),
                                fg="black", bg="#669966")
        self.total_days.place(x=10, y=420)
        self.ent_totalday = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                                  relief=GROOVE, bg="lightgray")
        self.ent_totalday.place(x=300, y=425)
        # ========days present======
        self.present = Label(self.fcontainer, text="Number of days present:", font=("times new roman", 20, "bold"),
                             fg="black", bg="#669966")
        self.present.place(x=10, y=490)
        self.ent_present = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                                 relief=GROOVE, bg="lightgray")
        self.ent_present.place(x=300, y=495)
        # =====absent days======
        self.absent = Label(self.fcontainer, text="Number of days absent:", font=("times new roman", 20, "bold"),
                            fg="black", bg="#669966")
        self.absent.place(x=10, y=560)
        self.ent_absent = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                                relief=GROOVE, bg="lightgray")
        self.ent_absent.place(x=300, y=565)

        # ======all buttons here=====
        self.btn_add = Button(self.fcontainer, text="ADD", font=("times new roman", 17, "bold"), bg="#2C3E4C",
                              fg="yellow",command=self.add).place(x=20, y=700, width=90)
        # ========update button====
        self.btn_update = Button(self.fcontainer, text="UPDATE", font=("times new roman", 17, "bold"),
                                 bg="#2C3E4C",
                                 fg="yellow",command=self.update).place(x=140, y=700, width=130)
        # =====delete=====
        self.btn_delete = Button(self.fcontainer, text="DELETE", font=("times new roman", 17, "bold"),
                                 bg="#2C3E4C",
                                 fg="yellow",command=self.delete).place(x=300, y=700, width=130)
        # =========clear========
        self.btn_clear = Button(self.fcontainer, text="CLEAR", font=("times new roman", 17, "bold"), bg="#2C3E4C",
                                fg="yellow",command=self.clear).place(x=460, y=700, width=90)

        scroll_x = Scrollbar(self.fourthcontainer, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.fourthcontainer, orient=VERTICAL)
        self.staffatten_table = ttk.Treeview(self.fourthcontainer, columns=(
                                                                     "First_Name", "Last_Name","Staff_ID_No"),
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.staffatten_table.xview)
        scroll_y.config(command=self.staffatten_table.yview)
        self.staffatten_table.heading("First_Name", text="First_Name")
        self.staffatten_table.heading("Last_Name", text="Last_Name")
        self.staffatten_table.heading("Staff_ID_No", text="Staff_ID_No")
        self.staffatten_table['show'] = "headings"
        self.staffatten_table.pack(fill=BOTH, expand=1)
        self.staffatten_table.bind("<ButtonRelease-1>", self.showdata_into_entry)
