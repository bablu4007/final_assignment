from tkinter import*
from tkinter import ttk
from back_end1.register_connection import*
from tkinter import messagebox
from model_class1.studentattendance_model import*
from tkcalendar import*
class Attendance:
    def __init__(self,screen):
        self.wn=screen
        self.wn.geometry("1480x830+50+0")
        self.wn.title("Student attendance".center(480))
        self.wn.config(background="#9900CC")
        self.con_studentattendence=register_database()
        self.from_date_var=StringVar()
        self.to_date_var=StringVar()
        # ======first frame=========
        self.fcontainer = Frame(self.wn, bg="violet", bd=10, relief=RIDGE)
        self.fcontainer.place(x=10, y=50, width=600, height=780)
        self.head2 = Label(self.fcontainer, text=" Attendance Details", font=("times new roman", 25, "bold"),
                           bg="violet", fg="black")
        self.head2.pack(side=TOP)
        # =====heading=======
        self.head1 = Label(self.wn, text="STUDENT ATTENDANCE", font=("times new roman", 30, "bold"), bg="#9900CC",fg="yellow")
        self.head1.place(x=700, y=0)
        # =======second container========
        self.scontainer = Frame(self.wn, bg="violet", bd=10, relief=RIDGE)
        self.scontainer.place(x=620, y=50, width=850, height=780)
        # =====third frame========
        self.tcontainer = Frame(self.scontainer, bg="light blue", bd=2, relief=GROOVE)
        self.tcontainer.place(x=0, y=0, width=827, height=50)

        # ====button for viewing all data=========
        self.view_btn = Button(self.tcontainer, text="View All Data", font=("arial", 15, "bold"), bd=5,
                               bg="yellow", command=self.view_window)
        self.view_btn.place(x=600, y=3, width=200, height=40)
        #=====calender button===
        self.calender_btn = Button(self.tcontainer, text="Calender", font=("arial", 15, "bold"), bd=10,
                               bg="black",fg="white",command=self.calc1)
        self.calender_btn.place(x=30, y=3, width=160, height=40)
        #=====get value1=====
        self.getvalue1_btn = Button(self.tcontainer, text="Get value1", font=("arial", 15, "bold"), bd=10,
                                   bg="black", fg="white", command=self.getvalue1)
        self.getvalue1_btn.place(x=220, y=3, width=160, height=40)
        #====get value2======
        self.getvalue2_btn = Button(self.tcontainer, text="Get value2", font=("arial", 15, "bold"), bd=10,
                                   bg="black", fg="white", command=self.getvalue2)
        self.getvalue2_btn.place(x=410, y=3, width=160, height=40)

        #====searching======
        lbl_search = Label(self.scontainer, text="Search By:", font=("times new roman", 25, "bold"), fg="black",
                           bg="violet")
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
        self.id = Label(self.fcontainer, text="Student_ID_No:", font=("times new roman", 20, "bold"),
                        fg="black", bg="violet")
        self.id.place(x=10, y=70)
        self.ent_id = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                            relief=GROOVE, bg="lightgray")
        self.ent_id.place(x=300, y=75)
        # ======first name======
        self.firstname = Label(self.fcontainer, text="First_Name:", font=("times new roman", 20, "bold"),
                               fg="black", bg="violet")
        self.firstname.place(x=10, y=140)
        self.ent_Name = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                              relief=GROOVE, bg="lightgray")
        self.ent_Name.place(x=300, y=145)
        # ===last name======
        self.lastname = Label(self.fcontainer, text="Last_Name:", font=("times new roman", 20, "bold"),
                              fg="black", bg="violet")
        self.lastname.place(x=10, y=210)
        self.ent_lname = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                               relief=GROOVE, bg="lightgray")
        self.ent_lname.place(x=300, y=215)
        # ====from=========
        self.from_date = Label(self.fcontainer, text="From:", font=("times new roman", 20, "bold"),
                               fg="black", bg="violet")
        self.from_date.place(x=10, y=280)
        self.ent_fromdate = Entry(self.fcontainer,textvariable=self.from_date_var, font=("arial", 12, "bold"), bd=1,
                               relief=GROOVE, bg="lightgray")
        self.ent_fromdate.place(x=300, y=285)
        # ======to=====
        self.to = Label(self.fcontainer, text="To:", font=("times new roman", 20, "bold"),
                               fg="black", bg="violet")
        self.to.place(x=10, y=350)
        self.ent_todate = Entry(self.fcontainer,textvariable=self.to_date_var, font=("arial", 12, "bold"), bd=1,
                               relief=GROOVE, bg="lightgray")
        self.ent_todate.place(x=300, y=355)
        # ====total days======
        self.total_days = Label(self.fcontainer, text="Total number of days:", font=("times new roman", 20, "bold"),
                             fg="black", bg="violet")
        self.total_days.place(x=10, y=420)
        self.ent_totalday = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                                    relief=GROOVE, bg="lightgray")
        self.ent_totalday.place(x=300, y=425)
        #========days present======
        self.present = Label(self.fcontainer, text="Number of days present:", font=("times new roman", 20, "bold"),
                             fg="black", bg="violet")
        self.present.place(x=10, y=490)
        self.ent_present = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                                    relief=GROOVE, bg="lightgray")
        self.ent_present.place(x=300, y=495)
        #=====absent days======
        self.absent = Label(self.fcontainer, text="Number of days absent:", font=("times new roman", 20, "bold"),
                             fg="black", bg="violet")
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
        self.sattent_table = ttk.Treeview(self.fourthcontainer, columns=("Student_ID_No",
                                                                     "First_Name", "Last_Name"),
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.sattent_table.xview)
        scroll_y.config(command=self.sattent_table.yview)
        self.sattent_table.heading("Student_ID_No", text="Student_ID_No")
        self.sattent_table.heading("First_Name", text="First_Name")
        self.sattent_table.heading("Last_Name", text="Last_Name")
        self.sattent_table['show'] = "headings"
        self.sattent_table.pack(fill=BOTH, expand=1)
        self.sattent_table.bind("<ButtonRelease-1>", self.showdata_into_entry)

    def calc1(self):
        self.calc = Calendar(self.wn, selectmode="day", date_pattern="yyyy/mm/dd")
        self.calc.place(x=520, y=345)
    def getvalue1(self):
        self.from_date_var.set(self.calc.get_date())

    def getvalue2(self):
        self.to_date_var.set(self.calc.get_date())

    def view_window(self):
        self.screen = Tk()
        self.screen.geometry("825x723+680+90")
        self.screen.config(bg="light green")
        # =====first frame inside view window=======
        self.view_frame = Frame(self.screen, bd=5, bg="white", relief=RIDGE)
        self.view_frame.place(x=10,y=130,width=805,height=580)
        # ========searching======
        lbl_search = Label(self.screen, text="Search By:", font=("times new roman", 25, "bold"), fg="maroon",
                           bg="violet")
        lbl_search.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.combo_search = ttk.Combobox(self.screen, width=13,
                                         font=("times new roman", 13, "bold"), state="readonly")
        self.combo_search["values"] = ("First_Name")
        self.combo_search.grid(row=0, column=1, padx=10, pady=10)
        self.search_ent = Entry(self.screen, font=("arial", 12, "bold"), bd=1, relief=GROOVE)
        self.search_ent.grid(row=0, column=2, padx=10, pady=10)
        search_btn = Button(self.screen, text="Search", font=("times new roman", 15, "bold"), bd=5, fg="black",
                            bg="white",
                            width=8,command=self.search_data1)
        search_btn.grid(row=0, column=3, padx=10, pady=10)
        searchall_btn = Button(self.screen, text="Search All", font=("times new roman", 15, "bold"), bd=5,
                               fg="black",
                               bg="white",
                               width=8,command=self.show_table)
        searchall_btn.grid(row=0, column=4, padx=10, pady=10)
        # =======sorting==========
        lbl_sort = Label(self.screen, text="Sort By:", font=("times new roman", 25, "bold"), fg="black",
                         bg="light green")
        lbl_sort.place(x=10, y=70)
        combo_sort = ttk.Combobox(self.screen, width=13,
                                  font=("times new roman", 13, "bold"), state="readonly")
        combo_sort["values"] = ("Student_ID_No")
        combo_sort.place(x=140, y=76, width=200)
        sort_btn = Button(self.screen, text="Sort", font=("times new roman", 15, "bold"), bd=5, fg="black",
                          bg="yellow",
                          width=8,command=self.sorting)
        sort_btn.place(x=380, y=70)
        #======scrollbar=========
        scroll_x = Scrollbar(self.view_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.view_frame, orient=VERTICAL)
        self.stu_table = ttk.Treeview(self.view_frame, columns=("Student_ID_No",
                                                                "First_Name", "Last_Name", "From","To","Total Number of days",
                                                                "Number of days present","Number of days absent"),
                                                                 xscrollcommand=scroll_x.set,
                                                                yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.stu_table .xview)
        scroll_y.config(command=self.stu_table .yview)
        self.stu_table .heading("Student_ID_No", text="Student_ID_No")
        self.stu_table .heading("First_Name", text="First_Name")
        self.stu_table .heading("Last_Name", text="Last_Name")
        self.stu_table .heading("From", text="From")
        self.stu_table .heading("To", text="To")
        self.stu_table .heading("Total Number of days", text="Total Number of days")
        self.stu_table .heading("Number of days present",text="Number of days present")
        self.stu_table .heading("Number of days absent", text="Number of days absent")
        self.stu_table ['show'] = "headings"
        self.stu_table .pack(fill=BOTH, expand=1)
        self.show_table()
        self.stu_table .bind("<ButtonRelease-1>", self.displaydata_into_entry)

    def search_data(self):
        try:
            query = "select ID_No,First_Name,Last_Name from tbl_student where " + str(
                self.combo_search1.get()) + "=" + str(self.search_ent1.get())
            row = self.con_studentattendence.select1(query)
            # print(row)
            if len(row) != 0:
                self.sattent_table.delete(*self.sattent_table.get_children())
                for i in row:
                    self.sattent_table.insert('', END, values=i)


        except Exception as es:

            messagebox.showerror("error",f"error due to {str(es)}")


    def showdata_into_entry(self,ev):
        row_cursor=self.sattent_table.focus()
        contents=self.sattent_table.item(row_cursor)
        row=contents['values']
        self.ent_id.delete(0, END)
        self.ent_id.insert(END,row[0])
        self.ent_Name.delete(0, END)
        self.ent_Name.insert(END,row[1])
        self.ent_lname.delete(0, END)
        self.ent_lname.insert(END,row[2])


    def add(self):
        if self.ent_id.get()=="" or self.ent_Name.get()=="" or self.ent_lname.get()=="" or \
                self.from_date_var.get()=="" or self.to_date_var.get()=="" or self.ent_totalday.get()=="" or \
                self.ent_present.get()=="" or self.ent_absent.get()=="":
            messagebox.showerror("Error","All fields are required")


        elif self.ent_id.get().isalpha() or self.ent_totalday.get().isalpha() or self.ent_present.get().isalpha() or \
                self.ent_absent.get().isalpha():
            messagebox.showerror("Error", "Alphabetical value is not allowed in staff id,total days, present days and absent days")
        else:
            try:

                stuattendance_obj=Model_studentattendance(self.ent_id.get(),self.ent_Name.get(),
                                                          self.ent_lname.get(),self.from_date_var.get(),
                                                          self.to_date_var.get(),self.ent_totalday.get(),
                                                          self.ent_present.get(),self.ent_absent.get())
                query="insert into tbl_student_attendance values(%s,%s,%s,%s,%s,%s,%s,%s);"
                values=(stuattendance_obj.get_ID_No(),stuattendance_obj.get_First_Name(),stuattendance_obj.get_Last_Name(),
                        stuattendance_obj.get_From(),stuattendance_obj.get_To(),stuattendance_obj.get_Total_days(),
                        stuattendance_obj.get_Days_present(),stuattendance_obj.get_Days_absent())
                self.con_studentattendence.insert(query,values)
                messagebox.showinfo("error","Data inserted in database successfully")
                self.clear()


            except Exception as e:
                messagebox.showerror("error",f"error due to {str(e)}")


    def show_table(self):
        query_select="select * from tbl_student_attendance;"
        row1=self.con_studentattendence.select1(query_select)
        if len(row1)!=0:
            self.stu_table.delete(*self.stu_table.get_children())
            for i in row1:
                self.stu_table.insert('',END,values=i)

    def clear(self):
        self.ent_id.delete(0,END)
        self.ent_Name.delete(0, END)
        self.ent_lname.delete(0, END)
        self.from_date_var.set("")
        self.to_date_var.set("")
        self.ent_totalday.delete(0, END)
        self.ent_present.delete(0,END)
        self.ent_absent.delete(0,END)

    def displaydata_into_entry(self,ev):
        row_cursor=self.stu_table.focus()
        contents=self.stu_table.item(row_cursor)
        row=contents['values']
        self.ent_id.delete(0, END)
        self.ent_id.insert(END, row[0])
        self.ent_Name.delete(0, END)
        self.ent_Name.insert(END, row[1])
        self.ent_lname.delete(0, END)
        self.ent_lname.insert(END, row[2])
        self.from_date_var.set(row[3])
        self.to_date_var.set(row[4])
        self.ent_totalday.delete(0, END)
        self.ent_totalday.insert(END, row[5])
        self.ent_present.delete(0, END)
        self.ent_present.insert(END, row[6])
        self.ent_absent.delete(0, END)
        self.ent_absent.insert(END, row[7])

    def delete(self):
        if self.ent_id.get() == "":
            messagebox.showerror("error", "please enter id nnumber to delete")
        else:

            try:
                query = "delete from tbl_student_attendance where Student_ID_No=%s;"
                stuattendance_obj=Model_studentattendance(self.ent_id.get(),self.ent_Name.get(),
                                                          self.ent_lname.get(),self.from_date_var.get(),
                                                          self.to_date_var.get(),self.ent_totalday.get(),
                                                          self.ent_present.get(),self.ent_absent.get())
                value = (stuattendance_obj.get_ID_No(),)
                self.con_studentattendence.delete(query, value)
                messagebox.showinfo("success", "data deleted successfully",parent=self.screen)
                self.show_table()
                self.clear()

            except Exception as es:
                messagebox.showerror("error", f"error due to {str(es)} ")

    def update(self):
        if self.ent_id.get() == "":
            messagebox.showerror("error", "please enter the student id to update student data")
        else:
            try:
                stuattendance_obj=Model_studentattendance(self.ent_id.get(),self.ent_Name.get(),self.ent_lname.get(),
                                                          self.from_date_var.get(),self.to_date_var.get(),self.ent_totalday.get(),
                                                          self.ent_present.get(),self.ent_absent.get())
                query = "update tbl_student_attendance set From_date=%s,To_date=%s,Total_days=%s,Present_days=%s,Absent_days=%s where " \
                        "Student_ID_No=%s;"
                values = (
                    stuattendance_obj.get_From(),stuattendance_obj.get_To(),stuattendance_obj.get_Total_days(),
                    stuattendance_obj.get_Days_present(),stuattendance_obj.get_Days_absent(),stuattendance_obj.get_ID_No())
                self.con_studentattendence.update(query, values)
                messagebox.showinfo("success", "Data updated successfully",parent=self.screen)
                self.show_table()
                self.clear()


            except Exception as es:
                messagebox.showerror("error", f"error due to {str(es)} ")

    def sorting(self):
        query = "select * from tbl_student_attendance;"
        records = self.con_studentattendence.select1(query)
        data_list1 = []
        for row in records:
            data_list1.append(row)
        d=self.bubblesort_ascending(data_list1)


    def bubblesort_ascending(self, list):
        for j in range(len(list)-1):
            for i in range(len(list)-1):
                if list[i] > list[i + 1]:
                    list[i],list[i+1]=list[i+1],list[i]
        messagebox.showinfo("success","list has been sorted in ascending order bu student id number",parent=self.screen)
        if len(list)!=0:
            self.stu_table.delete(*self.stu_table.get_children())
            for i in list:
                self.stu_table.insert('',END,values=i)

    def search_data1(self):
        query = "select First_Name from tbl_student_attendance;"
        records = self.con_studentattendence.select1(query)
        data_list = []
        for row in records:
            data_list.append(row[0])
        ans = self.linear_search(data_list, self.search_ent.get())
    def linear_search(self, data, item):
        for i in data:
            if i == item:
                messagebox.showinfo('Success', 'congrats Name exists in this list',parent=self.screen)
                query1 ="select * from tbl_student_attendance where First_Name=%s;"
                values1=(self.search_ent.get(),)
                records1 = self.con_studentattendence.select(query1,values1)
                if len(records1) != 0:
                    self.stu_table.delete(*self.stu_table.get_children())
                    for row in records1:
                        self.stu_table.insert('', END, values=row)

                break

        else:
            messagebox.showerror('error', 'sorry this Name doesnot exist in this list',parent=self.screen)




# window=Tk()
# Attendance(window)
# window.mainloop()