from tkinter import*
from tkinter import ttk
from model_class1.staff_model import*
from back_end1.register_connection import*
from tkinter import messagebox
class Staff:
    def __init__(self,screen):
        self.wn=screen
        self.wn.geometry("1480x830+50+0")
        self.wn.title("Staff management".center(450))
        self.wn.configure(background="#00FF00")
        self.con_staff=register_database()
        # =====heading=======
        self.head5 = Label(self.wn, text="STAFF   DATA", font=("times new roman", 30, "bold"), bg="#00FF00",
                           fg="maroon")
        self.head5.place(x=700, y=0)
        # ======first frame=========
        self.container_1 = Frame(self.wn, bg="#999999", bd=10, relief=RIDGE)
        self.container_1.place(x=10, y=50, width=600, height=780)
        self.head1 = Label(self.container_1, text=" Staff Details", font=("times new roman", 25, "bold"),
                          fg="gold",bg="#999999")
        self.head1.pack(side=TOP)
        #====id no==========
        self.id = Label(self.container_1, text="First_Name:", font=("times new roman", 20, "bold"),
                           fg="gold", bg="#999999")
        self.id.place(x=10, y=50)
        self.ent_fname = Entry(self.container_1, font=("arial", 12, "bold"), bd=1,
                               relief=GROOVE, bg="lightgray")
        self.ent_fname.place(x=220, y=50)
        # =======first name==========
        self.fname = Label(self.container_1, text="Last_Name:", font=("times new roman", 20, "bold"),
                           fg="gold", bg="#999999")
        self.fname.place(x=10, y=100)
        self.ent_lName = Entry(self.container_1, font=("arial", 12, "bold"), bd=1,
                               relief=GROOVE, bg="lightgray")
        self.ent_lName.place(x=220, y=100)
        # =======lname==========
        self.lName = Label(self.container_1, text=" Staff_ID_No:", font=("times new roman", 20, "bold"),
                           fg="gold", bg="#999999")
        self.lName.place(x=5, y=150)
        self.ent_id = Entry(self.container_1, font=("arial", 12, "bold"), bd=1,
                               relief=GROOVE, bg="lightgray")
        self.ent_id.place(x=220, y=150)

        # =======qualification==========
        self.qualification = Label(self.container_1, text="Qualification:", font=("times new roman", 20, "bold"),
                                    fg="gold", bg="#999999")
        self.qualification.place(x=10, y=350)
        self.ent_qualifi = Entry(self.container_1, font=("arial", 12, "bold"), bd=1,
                                   relief=GROOVE, bg="lightgray")
        self.ent_qualifi.place(x=220, y=350)
        # =======Email==========
        self.Email = Label(self.container_1, text="Email:", font=("times new roman", 20, "bold"),
                               fg="gold", bg="#999999")
        self.Email.place(x=10, y=400)
        self.ent_email = Entry(self.container_1, font=("arial", 12, "bold"), bd=1,
                                  relief=GROOVE, bg="lightgray")
        self.ent_email.place(x=220, y=400)
        # ======Salary=========
        self.salary = Label(self.container_1, text="Salary:", font=("times new roman", 20, "bold"),
                                 fg="gold", bg="#999999").place(x=10, y=200)
        self.ent_salary = Entry(self.container_1, font=("arial", 12, "bold"), bd=1, relief=GROOVE,
                                bg="lightgray")
        self.ent_salary.place(x=220, y=200)
        # ==========DOB====
        self.DOB = Label(self.container_1, text="DOB:", font=("times new roman", 20, "bold"),
                                 fg="gold", bg="#999999").place(x=10, y=450)
        self.ent_dob = Entry(self.container_1, font=("arial", 12, "bold"), bd=1, relief=GROOVE,
                                bg="lightgray")
        self.ent_dob.place(x=220, y=450)
        # ========courseID====
        a = self.list1()
        List = []
        for i in a:
            List.append(i[0])
        self.course1 = Label(self.container_1, text="Course_ID:", font=("times new roman", 20, "bold"),
                            fg="gold", bg="#999999").place(x=10, y=250)
        self.combo_course = ttk.Combobox(self.container_1, font=("arial", 12, "bold"))
        self.combo_course["values"] = List
        self.combo_course.place(x=220, y=250,width=190)
        # =========gender======
        self.gender1 = Label(self.container_1, text="Gender:", font=("times new roman", 20, "bold"),
                            fg="gold", bg="#999999").place(x=10, y=500)
        self.gen_combo=ttk.Combobox(self.container_1,font=("times new roman",15))
        self.gen_combo['values']=("Male","Female")
        self.gen_combo.place(x=220,y=500,width=190)
        # =====phone no===
        self.phone = Label(self.container_1, text="Phone_No:", font=("times new roman", 20, "bold"),
                           fg="gold", bg="#999999").place(x=10, y=300)
        self.ent_phone = Entry(self.container_1, font=("arial", 12, "bold"), bd=1, relief=GROOVE,
                               bg="lightgray")
        self.ent_phone.place(x=220, y=300)
        # =======religion===
        self.religion = Label(self.container_1, text="Subject:", font=("times new roman", 20, "bold"), bg="#999999",
                              fg="gold").place(x=10, y=550)

        self.combox3 = ttk.Combobox(self.container_1, font=("times new roman", 15))
        self.combox3['values'] = ("c++", "forensics", "python", "usabilty", "account", "basic maths", "information system","Algorithms","DBMS")
        self.combox3.place(x=220, y=550, width=190)
        # =======address=====
        self.address = Label(self.container_1, text="Address:", font=("times new roman", 20, "bold"),
                             fg="gold", bg="#999999").place(x=10, y=600)
        self.txt = Text(self.container_1, width=35, height=5, bg="lightgray")
        self.txt.place(x=220, y=600)
        # ==========add button====
        self.btn_add1 = Button(self.container_1, text="ADD", font=("times new roman", 17, "bold"), bg="#2C3E4C",
                              fg="gold",command=self.add).place(x=0, y=700, width=90)
        # ========update button====
        self.btn_update1 = Button(self.container_1, text="UPDATE", font=("times new roman", 17, "bold"),
                                 bg="#2C3E4C",
                                 fg="gold",command=self.update).place(x=120, y=700, width=130)
        # =====delete=====
        self.btn_delete1 = Button(self.container_1, text="DELETE", font=("times new roman", 17, "bold"),
                                 bg="#2C3E4C",
                                 fg="gold",command=self.delete).place(x=280, y=700, width=130)
        # =========clear========
        self.btn_clear1 = Button(self.container_1, text="CLEAR", font=("times new roman", 17, "bold"), bg="#2C3E4C",
                                fg="gold",command=self.cut).place(x=440, y=700, width=90)

        self.container_2 = Frame(self.wn, bg="#999999", bd=10, relief=RIDGE)
        self.container_2.place(x=620, y=50, width=850, height=780)
        #====frame under frame====
        self.container_3 = Frame(self.container_2, bg="white", bd=10, relief=RIDGE)
        self.container_3.place(x=10, y=120, width=810, height=630)
        # =======sorting==========
        lbl_sort = Label(self.container_2, text="Sort By:", font=("times new roman", 20, "bold"), fg="black",
                         bg="#999999")
        lbl_sort.place(x=10, y=70)
        combo_sort = ttk.Combobox(self.container_2, width=13,
                                  font=("times new roman", 13, "bold"), state="readonly")
        combo_sort["values"] = ("First_Name")
        combo_sort.place(x=140, y=76, width=200)
        sort_btn = Button(self.container_2, text="Sort", font=("times new roman", 15, "bold"), bd=5, fg="black",
                          bg="yellow",
                          width=8,command=self.sorting)
        sort_btn.place(x=380, y=70)
        #====searching=========
        lbl_search = Label(self.container_2, text="Search By:", font=("times new roman", 25, "bold"), fg="gold",
                           bg="#999999")
        lbl_search.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.combo_search = ttk.Combobox(self.container_2, width=13,
                                    font=("times new roman", 13, "bold"), state="readonly")
        self.combo_search["values"] = ("First_Name")
        self.combo_search.grid(row=0, column=1, padx=10, pady=10)
        self.search_ent = Entry(self.container_2, font=("arial", 12, "bold"), bd=1, relief=GROOVE)
        self.search_ent.grid(row=0, column=2, padx=10, pady=10)
        search_btn = Button(self.container_2, text="Search", font=("times new roman", 15, "bold"), bd=5, fg="black",
                            bg="white",
                            width=8,command=self.search_data2)
        search_btn.grid(row=0, column=3, padx=10, pady=10)
        searchall_btn = Button(self.container_2, text="Search All", font=("times new roman", 15, "bold"), bd=5,
                               fg="black",
                               bg="white",
                               width=8,command=self.show_table)
        searchall_btn.grid(row=0, column=4, padx=10, pady=10)
        scroll_x = Scrollbar(self.container_3, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.container_3, orient=VERTICAL)
        self.staff_table = ttk.Treeview(self.container_3, columns=(
            "First_Name", "Last_Name","ID_No", "Salary", "Course_ID", "Phone_No", "Qualification", "Email",
            "DOB", "Gender", "Subject", "Address"),
                                         xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.staff_table.xview)
        scroll_y.config(command=self.staff_table.yview)
        self.staff_table.heading("First_Name", text="First_Name")
        self.staff_table.heading("Last_Name", text="Last_Name")
        self.staff_table.heading("ID_No", text="ID_No")
        self.staff_table.heading("Salary", text="Salary")
        self.staff_table.heading("Course_ID", text="Course_ID")
        self.staff_table.heading("Phone_No", text="Phone_No")
        self.staff_table.heading("Qualification", text="Qualification")
        self.staff_table.heading("Email", text="Email")
        self.staff_table.heading("DOB", text="DOB")
        self.staff_table.heading("Gender", text="Gender")
        self.staff_table.heading("Subject", text="Subject")
        self.staff_table.heading("Address", text="Address")
        self.staff_table['show'] = "headings"
        self.staff_table.pack(fill=BOTH,expand=1)
        self.show_table()
        self.staff_table.bind("<ButtonRelease-1>", self.show_data_entry)

    def list1(self):
        query="select Course_ID from tbl_course;"
        row=self.con_staff.select1(query)
        return row

    def add(self):
        if self.ent_id.get()=="" or self.ent_fname.get()=="" or self.ent_salary.get()=="" or self.combo_course.get()=="" or\
                self.ent_phone.get()=="" or self.ent_qualifi.get()=="" or self.ent_email.get()=="" or self.ent_dob.get()=="" or \
                self.gen_combo.get()=="" or self.combox3.get()=="" or self.txt.get('1.0',END)=="":
            messagebox.showerror("Error","All fields are required")

        elif self.ent_fname.get().isdigit() or self.ent_lName.get().isdigit():
            messagebox.showerror("error","integer value is not allowed in first name and last name")

        elif self.ent_phone.get().isalpha() or self.ent_id.get().isalpha() or self.ent_salary.get().isalpha():
            messagebox.showerror("Error", "Alphabetical value is not allowed in contact number,staff ID and salary, please enter number value only")

        else:
            try:
                staff_obj=Model_staff(self.ent_fname.get(),self.ent_lName.get(),self.ent_id.get(),self.ent_salary.get(),
                                      self.combo_course.get(),self.ent_phone.get(),self.ent_qualifi.get(),self.ent_email.get(),
                                      self.ent_dob.get(),self.gen_combo.get(),self.combox3.get(),self.txt.get('1.0',END))
                query="insert into tbl_staff1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                values=(staff_obj.get_First_Name(),staff_obj.get_Last_Name(),staff_obj.get_ID_No(),staff_obj.get_Salary(),
                        staff_obj.get_Course_ID(),staff_obj.get_Phone_No(),staff_obj.get_Qualification(),staff_obj.get_Email(),
                        staff_obj.get_DOB(),staff_obj.get_Gender(),staff_obj.get_Subject(),staff_obj.get_Address())
                self.con_staff.insert(query,values)
                messagebox.showinfo("success","Data inserted successfully")
                self.show_table()
                self.cut()

            except Exception as error:
                messagebox.showerror("error",f"Error due to {str(error)}")

    def cut(self):
        self.ent_fname.delete(0,END)
        self.ent_id.delete(0,END)
        self.ent_lName.delete(0,END)
        self.ent_salary.delete(0,END)
        self.combo_course.delete(0,END)
        self.ent_phone.delete(0, END)
        self.ent_qualifi.delete(0, END)
        self.ent_email.delete(0, END)
        self.ent_dob.delete(0, END)
        self.gen_combo.delete(0, END)
        self.combox3.delete(0,END)
        self.txt.delete("1.0", END)

    def show_table(self):
        query_select="select * from tbl_staff1;"
        row1=self.con_staff.select1(query_select)
        if len(row1)!=0:
            self.staff_table.delete(*self.staff_table.get_children())
            for i in row1:
                self.staff_table.insert('',END,values=i)

    def show_data_entry(self,ev):
        row_cursor=self.staff_table.focus()
        contents=self.staff_table.item(row_cursor)
        row=contents['values']
        self.ent_fname.delete(0,END)
        self.ent_fname.insert(END,row[0])
        self.ent_lName.delete(0,END)
        self.ent_lName.insert(END,row[1])
        self.ent_id.delete(0, END)
        self.ent_id.insert(END, row[2])
        self.ent_salary.delete(0,END)
        self.ent_salary.insert(END,row[3])
        self.combo_course.delete(0,END)
        self.combo_course.insert( END,row[4])
        self.ent_phone.delete(0, END)
        self.ent_phone.insert( END,row[5])
        self.ent_qualifi.delete(0, END)
        self.ent_qualifi.insert(END,row[6])
        self.ent_email.delete(0, END)
        self.ent_email.insert( END,row[7])
        self.ent_dob.delete(0, END)
        self.ent_dob.insert( END,row[8])
        self.gen_combo.delete(0, END)
        self.gen_combo.insert( END,row[9])
        self.combox3.delete(0,END)
        self.combox3.insert( END,row[10])
        self.txt.delete("1.0", END)
        self.txt.insert( END,row[11])

    def update(self):
        if self.ent_id.get()=="":
            messagebox.showerror("error","please enter the student id to update student data")
        else:
            try:
                staff_obj=Model_staff(self.ent_fname.get(),self.ent_lName.get(),self.ent_id.get(),self.ent_salary.get(),
                                      self.combo_course.get(),self.ent_phone.get(),self.ent_qualifi.get(),self.ent_email.get(),
                                      self.ent_dob.get(),self.gen_combo.get(),self.combox3.get(),self.txt.get('1.0',END))
                query="update tbl_staff1 set First_Name=%s,Last_Name=%s,Salary=%s,Course_ID=%s,Phone_No=%s,Qualification=%s,Email=%s," \
                      "DOB=%s,Gender=%s,Subject=%s,Address=%s where ID_No=%s;"
                values = (
                staff_obj.get_First_Name(),staff_obj.get_Last_Name(),staff_obj.get_Salary(),staff_obj.get_Course_ID(),
                staff_obj.get_Phone_No(),staff_obj.get_Qualification(),staff_obj.get_Email(),staff_obj.get_DOB(),
                staff_obj.get_Gender(),staff_obj.get_Subject(),staff_obj.get_Address(),staff_obj.get_ID_No())
                self.con_staff.update(query, values)
                messagebox.showinfo("success","Data updated successfully")
                self.show_table()
                self.cut()


            except Exception as es:
                messagebox.showerror("error",f"error due to {str(es)} ")

    def delete(self):
        if self.ent_id.get()=="":
            messagebox.showerror("error","please enter staff id number to delete that staff data")
        else:

            try:
                query="delete from tbl_staff1 where ID_No=%s;"
                staff_obj=Model_staff(self.ent_fname.get(),self.ent_lName.get(),self.ent_id.get(),self.ent_salary.get(),
                                      self.combo_course.get(),self.ent_phone.get(),self.ent_qualifi.get(),self.ent_email.get(),
                                      self.ent_dob.get(),self.gen_combo.get(),self.combox3.get(),self.txt.get('1.0',END))
                value=(staff_obj.get_ID_No(),)
                self.con_staff.delete(query,value)
                messagebox.showinfo("success","data deleted successfully")
                self.show_table()
                self.cut()

            except Exception as es:
                messagebox.showerror("error",f"error due to {str(es)} ")

    def search_data2(self):
        query = "select First_Name from tbl_staff1;"
        records = self.con_staff.select1(query)
        data_list = []
        for row in records:
            data_list.append(row[0])
        ans = self.linear_search(data_list, self.search_ent.get())

    def linear_search(self, data, item):
        for i in data:
            if i == item:
                messagebox.showinfo('Success', 'congrats staff having this name  exists in this list')
                query1 = "select * from tbl_staff1 where First_Name=%s;"
                values1 = (self.search_ent.get(),)
                records1 = self.con_staff.select(query1, values1)
                if len(records1) != 0:
                    self.staff_table.delete(*self.staff_table.get_children())
                    for i in records1:
                        self.staff_table.insert("", END, values=i)

                break

        else:
            messagebox.showerror('error', 'sorry staff having this name doesnot exist in this list')


    def sorting(self):
        query = "select * from tbl_staff1;"
        records = self.con_staff.select1(query)
        data_list1 = []
        for row in records:
            data_list1.append(row)
        d = self.bubblesort_ascending(data_list1)

    def bubblesort_ascending(self, list):
        for j in range(len(list) - 1):
            for i in range(len(list) - 1):
                if list[i] > list[i + 1]:
                    list[i], list[i + 1] = list[i + 1], list[i]
        if len(list) != 0:
            self.staff_table.delete(*self.staff_table.get_children())
            for i in list:
                self.staff_table.insert('', END, values=i)

# window=Tk()
# Staff(window)
# window.mainloop()