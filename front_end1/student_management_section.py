from tkinter import *
from tkinter import ttk
from back_end1.register_connection import *
from model_class1.student_model import *
from tkinter import messagebox
from tkcalendar import *


class Student:
    def __init__(self, screen):
        self.wn = screen
        self.wn.geometry("1480x830+50+0")
        self.wn.title("student management".center(450))
        self.wn.configure(background="light green")
        self.con_student = register_database()

        self.admission_var = StringVar()
        self.dob_var = StringVar()
        # =====heading=======
        self.head5 = Label(self.wn, text="STUDENT   DATA", font=("times new roman", 30, "bold"), bg="light green",
                           fg="maroon")
        self.head5.place(x=800, y=0)
        self.container_1 = Frame(self.wn, bg="lightskyblue", bd=0, relief=RIDGE)
        self.container_1.place(x=10, y=50, width=720, height=780)
        # ====calender=====
        self.btn_caleder = Button(self.container_1, text="Get value1", font=("times new roman", 17, "bold"),
                                  bg="orange",
                                  fg="black", bd=2, command=self.date_cal).place(x=550, y=400, width=110)
        self.btn_caleder2 = Button(self.container_1, text="Get value2", font=("times new roman", 17, "bold"),
                                   bg="orange",
                                   fg="black", bd=2, command=self.date_cal1).place(x=550, y=450, width=110)

        # =====heading=======
        self.head = Label(self.container_1, text="Student Details", font=("times new roman", 30, "bold"), fg="maroon",
                          bg="lightskyblue")
        self.head.pack(side=TOP)
        # =======ID==========
        self.ID = Label(self.container_1, text="Student_ID_No:", font=("times new roman", 20, "bold"),
                        fg="white", bg="lightskyblue")
        self.ID.place(x=10, y=100)
        self.ent_ID = Entry(self.container_1, font=("arial", 12, "bold"), bd=1,
                            relief=GROOVE, bg="lightgray")
        self.ent_ID.place(x=260, y=100)
        # =======name==========
        self.Name = Label(self.container_1, text="First Name:", font=("times new roman", 20, "bold"),
                          fg="white", bg="lightskyblue")
        self.Name.place(x=10, y=150)
        self.ent_Name = Entry(self.container_1, font=("arial", 12, "bold"), bd=1,
                              relief=GROOVE, bg="lightgray")
        self.ent_Name.place(x=260, y=150)

        # =======Admission date==========
        self.Admission_date = Label(self.container_1, text="Admission Date:", font=("times new roman", 20, "bold"),
                                    fg="white", bg="lightskyblue")
        self.Admission_date.place(x=10, y=50)
        self.ent_admission = Entry(self.container_1, textvariable=self.admission_var, font=("arial", 12, "bold"), bd=1,
                                   relief=GROOVE,
                                   bg="lightgray")
        self.ent_admission.place(x=260, y=60, width=184, height=25)
        # =======father name==========
        self.father_name = Label(self.container_1, text="Father's_Name:", font=("times new roman", 20, "bold"),
                                 fg="white", bg="lightskyblue")
        self.father_name.place(x=10, y=400)
        self.ent_fathername = Entry(self.container_1, font=("arial", 12, "bold"), bd=1,
                                    relief=GROOVE, bg="lightgray")
        self.ent_fathername.place(x=260, y=400)
        # ======last name=========
        self.last_name = Label(self.container_1, text="Last_Name:", font=("times new roman", 20, "bold"),
                               fg="white", bg="lightskyblue").place(x=10, y=200)
        self.ent_lastname = Entry(self.container_1, font=("arial", 12, "bold"), bd=1, relief=GROOVE,
                                  bg="lightgray")
        self.ent_lastname.place(x=260, y=200)
        # ==========mother name====
        self.mother_name = Label(self.container_1, text="Mother's_Name:", font=("times new roman", 20, "bold"),
                                 fg="white", bg="lightskyblue").place(x=10, y=450)
        self.ent_mother = Entry(self.container_1, font=("arial", 12, "bold"), bd=1, relief=GROOVE,
                                bg="lightgray")
        self.ent_mother.place(x=260, y=450)
        # ========DOB=======

        self.dob = Label(self.container_1, text="Date Of Birth:", font=("times new roman", 20, "bold"),
                         fg="white", bg="lightskyblue").place(x=10, y=250)
        self.ent_dob = Entry(self.container_1, textvariable=self.dob_var, font=("arial", 12, "bold"), bd=1,
                             relief=GROOVE,
                             bg="lightgray")
        self.ent_dob.place(x=260, y=250, width=184, height=25)

        # =========gender======
        self.gender = Label(self.container_1, text="Gender:", font=("times new roman", 20, "bold"),
                            fg="white", bg="lightskyblue").place(x=10, y=500)
        self.combu = ttk.Combobox(self.container_1, font=("times new roman", 12, "bold"))
        self.combu["values"] = ("Male", "Female")
        self.combu.place(x=260, y=500, width=190)
        # ========courseID====
        a = self.list()
        List = []
        for i in a:
            List.append(i[0])

        self.course = Label(self.container_1, text="Course_ID:", font=("times new roman", 20, "bold"),
                            fg="white", bg="lightskyblue").place(x=10, y=300)
        self.combo_course = ttk.Combobox(self.container_1, font=("arial", 12, "bold"))
        self.combo_course["values"] = List
        self.combo_course.place(x=260, y=300, width=190)
        # ======section====
        self.section = Label(self.container_1, text="Section:", font=("times new roman", 20, "bold"), bg="lightskyblue",
                             fg="white").place(x=10, y=550)

        self.combox2 = ttk.Combobox(self.container_1, font=("times new roman", 15))
        self.combox2['values'] = ("Select", "30A", "30B", "31A", "31B", "32A", "32B")
        self.combox2.place(x=260, y=550, width=190)
        # =====phone no===

        self.phone = Label(self.container_1, text="Phone_No:", font=("times new roman", 20, "bold"),
                           fg="white", bg="lightskyblue").place(x=10, y=350)
        self.ent_phone = Entry(self.container_1, font=("arial", 12, "bold"), bd=1, relief=GROOVE,
                               bg="lightgray")
        self.ent_phone.place(x=260, y=350)
        # =======address=====
        self.address = Label(self.container_1, text="Address:", font=("times new roman", 20, "bold"),
                             fg="white", bg="lightskyblue").place(x=10, y=600)
        self.txt = Text(self.container_1, width=35, height=5, bg="lightgray")
        self.txt.place(x=260, y=600)
        self.container_2 = Frame(self.wn, bg="lightskyblue", bd=5, relief=RIDGE)
        self.container_2.place(x=740, y=50, width=730, height=780)
        # ====frame under frame====
        self.container_3 = Frame(self.container_2, bg="white", bd=5, relief=RIDGE)
        self.container_3.place(x=10, y=120, width=710, height=630)

        # =======sorting==========
        lbl_sort = Label(self.container_2, text="Sort By:", font=("times new roman", 20, "bold"), fg="black",
                         bg="lightskyblue")
        lbl_sort.place(x=10, y=70)
        self.combo_sort = ttk.Combobox(self.container_2, width=13,
                                       font=("times new roman", 13, "bold"), state="readonly")
        self.combo_sort["values"] = ("Admission_date")
        self.combo_sort.place(x=140, y=76, width=150)
        sort_btn = Button(self.container_2, text="Sort", font=("times new roman", 15, "bold"), bd=5, fg="black",
                          bg="yellow",
                          width=8, command=self.sorting)
        sort_btn.place(x=370, y=70)
        # ========searching======
        lbl_search = Label(self.container_2, text="Search By:", font=("times new roman", 25, "bold"), fg="yellow",
                           bg="lightskyblue")
        lbl_search.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.combo_search = ttk.Combobox(self.container_2, width=13,
                                         font=("times new roman", 13, "bold"), state="readonly")
        self.combo_search["values"] = ("First_Name")
        self.combo_search.grid(row=0, column=1, padx=10, pady=10)
        self.search_ent = Entry(self.container_2, font=("arial", 12, "bold"), bd=1, relief=GROOVE)
        self.search_ent.grid(row=0, column=2, padx=10, pady=10)
        search_btn = Button(self.container_2, text="Search", font=("times new roman", 15, "bold"), bd=5, fg="black",
                            bg="white",
                            width=8, command=self.search_data)
        search_btn.place(x=550, y=10)
        searchall_btn = Button(self.container_2, text="Search All", font=("times new roman", 15, "bold"), bd=5,
                               fg="black",
                               bg="white",
                               width=8, command=self.show_table)
        searchall_btn.place(x=550, y=70)
        self.btn_add = Button(self.container_1, text="ADD", font=("times new roman", 17, "bold"), bg="#2C3E4C",
                              fg="yellow", command=self.add).place(x=20, y=700, width=90)
        # ========update button====
        self.btn_update = Button(self.container_1, text="UPDATE", font=("times new roman", 17, "bold"),
                                 bg="#2C3E4C",
                                 fg="yellow", command=self.update).place(x=140, y=700, width=130)
        # =====delete=====
        self.btn_delete = Button(self.container_1, text="DELETE", font=("times new roman", 17, "bold"),
                                 bg="#2C3E4C",
                                 fg="yellow", command=self.delete).place(x=300, y=700, width=130)
        # =========clear========
        self.btn_clear = Button(self.container_1, text="CLEAR", font=("times new roman", 17, "bold"), bg="#2C3E4C",
                                fg="yellow", command=self.clear).place(x=460, y=700, width=90)

        scroll_x = Scrollbar(self.container_3, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.container_3, orient=VERTICAL)
        self.student_table = ttk.Treeview(self.container_3, columns=(
            "Admission Date", "ID_No", "First Name", "Last_Name", "Date Of Birth", "Course_ID", "Phone_No",
            "Father's_Name",
            "Mother's_Name", "Gender", "Section", "Address"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("Admission Date", text="Admission Date")
        self.student_table.heading("ID_No", text="ID_No")
        self.student_table.heading("First Name", text="First Name")
        self.student_table.heading("Last_Name", text="Last_Name")
        self.student_table.heading("Date Of Birth", text="Date Of Birth")
        self.student_table.heading("Course_ID", text="Course_ID")
        self.student_table.heading("Phone_No", text="Phone_No")
        self.student_table.heading("Father's_Name", text="Father's_Name")
        self.student_table.heading("Mother's_Name", text="Mother's_Name")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Section", text="Section")
        self.student_table.heading("Address", text="Address")
        self.student_table['show'] = "headings"
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.column("Admission Date", width=120)
        self.student_table.column("ID_No", width=100)
        self.student_table.column("First Name", width=150)
        self.student_table.column("Last_Name", width=150)
        self.student_table.column("Date Of Birth", width=150)
        self.student_table.column("Course_ID", width=150)
        self.student_table.column("Phone_No", width=150)
        self.student_table.column("Father's_Name", width=150)
        self.student_table.column("Mother's_Name", width=150)
        self.student_table.column("Gender", width=150)
        self.student_table.column("Section", width=150)
        self.student_table.column("Address", width=150)
        self.show_table()
        self.student_table.bind("<ButtonRelease-1>", self.show_data_entry)
        self.calc = Calendar(self.wn, selectmode="day", date_pattern="yyyy/mm/dd")
        self.calc.place(x=470, y=250)

    def date_cal1(self):
        self.dob_var.set(self.calc.get_date())

    def date_cal(self):
        self.admission_var.set(self.calc.get_date())

    def list(self):
        query = "select Course_ID from tbl_course;"
        row = self.con_student.select1(query)
        return row

    def add(self):
        if self.admission_var.get() == "" or self.ent_ID.get() == "" or self.ent_Name.get() == "" or self.ent_lastname.get() == "" \
                or self.dob_var.get() == "" or self.combo_course.get() == "" or self.ent_phone.get() == "" or \
                self.ent_fathername.get() == "" or self.ent_mother.get() == "" or self.combu.get() == "" or self.combox2.get() == "" \
                or self.txt.get("1.0", END) == "":
            messagebox.showerror("Error", "All fields are required")

        elif self.ent_Name.get().isdigit() or self.ent_lastname.get().isdigit() or self.ent_fathername.get().isdigit() or \
                self.ent_mother.get().isdigit():
            messagebox.showerror("error",
                                 "integer value is not allowed in first name ,last name, father's name and mother's name")

        elif self.ent_phone.get().isalpha() or self.ent_ID.get().isalpha():
            messagebox.showerror("Error",
                                 "Alphabetical value is not allowed in contact number and student ID, please enter numbervalue only")
        else:
            try:

                stu_obj = Model_student(self.admission_var.get(), self.ent_ID.get(), self.ent_Name.get(),
                                        self.ent_lastname.get(),
                                        self.dob_var.get(), self.combo_course.get(), self.ent_phone.get(),
                                        self.ent_fathername.get(),
                                        self.ent_mother.get(), self.combu.get(), self.combox2.get(),
                                        self.txt.get("1.0", END))
                query = "insert into tbl_student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                values = (
                stu_obj.get_Admission_date(), stu_obj.get_ID_No(), stu_obj.get_First_Name(), stu_obj.get_Last_Name(),
                stu_obj.get_DOB(), stu_obj.get_Course_ID(), stu_obj.get_Phone_No(), stu_obj.get_Father_Name(),
                stu_obj.get_Mother_Name(), stu_obj.get_Gender(), stu_obj.get_Section(), stu_obj.get_Address())
                self.con_student.insert(query, values)
                messagebox.showinfo("success", "Data inserted in database successfully")
                self.show_table()
                self.clear()


            except Exception as e:
                messagebox.showerror("error", f"error due to {str(e)}")

    def clear(self):
        self.admission_var.set("")
        self.ent_ID.delete(0, END)
        self.ent_Name.delete(0, END)
        self.ent_lastname.delete(0, END)
        self.dob_var.set("")
        self.combo_course.delete(0, END)
        self.ent_phone.delete(0, END)
        self.ent_fathername.delete(0, END)
        self.ent_mother.delete(0, END)
        self.combu.delete(0, END)
        self.combox2.delete(0, END)
        self.txt.delete("1.0", END)

    def show_table(self):
        query_select = "select * from tbl_student;"
        row1 = self.con_student.select1(query_select)
        if len(row1) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in row1:
                self.student_table.insert('', END, values=i)

    def show_data_entry(self, ev):
        row_cursor = self.student_table.focus()
        contents = self.student_table.item(row_cursor)
        row = contents['values']
        self.admission_var.set(row[0])
        self.ent_ID.delete(0, END)
        self.ent_ID.insert(END, row[1])
        self.ent_Name.delete(0, END)
        self.ent_Name.insert(END, row[2])
        self.ent_lastname.delete(0, END)
        self.ent_lastname.insert(END, row[3])
        self.dob_var.set(row[4])
        self.combo_course.delete(0, END)
        self.combo_course.insert(END, row[5])
        self.ent_phone.delete(0, END)
        self.ent_phone.insert(END, row[6])
        self.ent_fathername.delete(0, END)
        self.ent_fathername.insert(END, row[7])
        self.ent_mother.delete(0, END)
        self.ent_mother.insert(END, row[8])
        self.combu.delete(0, END)
        self.combu.insert(END, row[9])
        self.combox2.delete(0, END)
        self.combox2.insert(END, row[10])
        self.txt.delete("1.0", END)
        self.txt.insert(END, row[11])

    def update(self):
        if self.ent_ID.get() == "":
            messagebox.showerror("error", "please enter the student id to update student data")
        else:
            try:
                stu_obj = Model_student(self.admission_var.get(), self.ent_ID.get(), self.ent_Name.get(),
                                        self.ent_lastname.get(), self.dob_var.get(), self.combo_course.get(),
                                        self.ent_phone.get(), self.ent_fathername.get(), self.ent_mother.get(),
                                        self.combu.get(), self.combox2.get(), self.txt.get("1.0", END))
                query = "update tbl_student set Admission_date=%s,First_Name=%s,Last_Name=%s,DOB=%s,Course_ID=%s,Phone_No=%s," \
                        "Father_Name=%s,Mother_Name=%s,Gender=%s,Section=%s,Address=%s where ID_No=%s;"
                values = (
                    stu_obj.get_Admission_date(), stu_obj.get_First_Name(), stu_obj.get_Last_Name(),
                    stu_obj.get_DOB(), stu_obj.get_Course_ID(), stu_obj.get_Phone_No(), stu_obj.get_Father_Name(),
                    stu_obj.get_Mother_Name(), stu_obj.get_Gender(), stu_obj.get_Section(), stu_obj.get_Address(),
                    stu_obj.get_ID_No())
                self.con_student.update(query, values)
                messagebox.showinfo("success", "Data updated successfully")
                self.show_table()
                self.clear()


            except Exception as es:
                messagebox.showerror("error", f"error due to {str(es)} ")

    def delete(self):
        if self.ent_ID.get() == "":
            messagebox.showerror("error", "please enter id number to delete")
        else:

            try:
                query = "delete from tbl_student where ID_No=%s;"
                stu_obj = Model_student(self.admission_var.get(), self.ent_ID.get(), self.ent_Name.get(),
                                        self.ent_lastname.get(), self.dob_var.get(), self.combo_course.get(),
                                        self.ent_phone.get(), self.ent_fathername.get(), self.ent_mother.get(),
                                        self.combu.get(), self.combox2.get(), self.txt.get("1.0", END))
                value = (stu_obj.get_ID_No(),)
                self.con_student.delete(query, value)
                messagebox.showinfo("success", "data deleted successfully")
                self.show_table()
                self.clear()


            except Exception as es:
                messagebox.showerror("error", f"error due to {str(es)} ")

    def search_data(self):
        query = "select First_Name from tbl_student;"
        records = self.con_student.select1(query)
        data_list = []
        for row in records:
            data_list.append(row[0])
        ans = self.linear_search(data_list, self.search_ent.get())

    def linear_search(self, data, item):
        for i in data:
            if i == item:
                messagebox.showinfo('Success', 'congrats Name exists in this list')
                query1 = "select * from tbl_student  where First_Name=%s;"
                values1 = (self.search_ent.get(),)
                records1 = self.con_student.select(query1, values1)
                if len(records1) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in records1:
                        self.student_table.insert('', END, values=i)

                break

        else:
            messagebox.showerror('error', 'sorry this Name doesnot exist in this list')

    def sorting(self):
        query = "select * from tbl_student;"
        records = self.con_student.select1(query)
        data_list1 = []
        for row in records:
            data_list1.append(row)
        d = self.bubblesort_ascending(data_list1)

    def bubblesort_ascending(self, list):
        for j in range(len(list) - 1):
            for i in range(len(list) - 1):
                if list[i] > list[i + 1]:
                    list[i], list[i + 1] = list[i + 1], list[i]
        messagebox.showinfo("success", "the list has been sorted by Firstname in ascending order")
        if len(list) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in list:
                self.student_table.insert('', END, values=i)

# window=Tk()
# Student(window)
# window.mainloop()