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
        self.fcontainer = Frame(self.wn, bg="salmon", bd=10, relief=RIDGE)
        self.fcontainer.place(x=10, y=10, width=600, height=820)
        self.head2 = Label(self.fcontainer, text=" Student Fees Details", font=("times new roman", 25, "bold"),
                           bg="salmon",fg="black")
        self.head2.pack(side=TOP)
        # =====heading=======
        self.head1 = Label(self.wn, text="STUDENT  FEES", font=("times new roman", 30, "bold"), bg="#003333",
                           fg="red")
        self.head1.place(x=700, y=0)
        #=======second container========
        self.scontainer=Frame(self.wn, bg="salmon", bd=10, relief=RIDGE)
        self.scontainer.place(x=620,y=50,width=850,height=780)
        #=====third frame========
        self.tcontainer=Frame(self.scontainer,bg="light blue",bd=2,relief=GROOVE)
        self.tcontainer.place(x=0,y=0,width=827,height=50)

        #====button for viewing all data=========
        self.view_btn=Button(self.tcontainer,text="View All Data",font=("arial",15,"bold"),bd=5,bg="light green",command=self.view_window)
        self.view_btn.place(x=300,y=3,width=200,height=40)

        #====searching========
        lbl_search = Label(self.scontainer, text="Search By:", font=("times new roman", 25, "bold"), fg="yellow",
                           bg="salmon")
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
                        fg="yellow", bg="salmon")
        self.id.place(x=10, y=70)
        self.ent_id = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                              relief=GROOVE, bg="lightgray")
        self.ent_id.place(x=260, y=75)
        #======first name======
        self.firstname = Label(self.fcontainer, text="First_Name:", font=("times new roman", 20, "bold"),
                        fg="yellow", bg="salmon")
        self.firstname.place(x=10, y=140)
        self.ent_Name = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                              relief=GROOVE, bg="lightgray")
        self.ent_Name.place(x=260, y=145)
        #===last name======
        self.lastname = Label(self.fcontainer, text="Last_Name:", font=("times new roman", 20, "bold"),
                               fg="yellow", bg="salmon")
        self.lastname.place(x=10, y=210)
        self.ent_lname = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                              relief=GROOVE, bg="lightgray")
        self.ent_lname.place(x=260, y=215)
        #====total fees=========
        self.fee = Label(self.fcontainer, text="Total Fees:", font=("times new roman", 20, "bold"),
                              fg="yellow", bg="salmon")
        self.fee.place(x=10, y=280)
        self.ent_fee = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                              relief=GROOVE, bg="lightgray")
        self.ent_fee.place(x=260, y=285)
        #======semester=====
        self.semester = Label(self.fcontainer, text="Semester:", font=("times new roman", 20, "bold"),
                              fg="yellow", bg="salmon")
        self.semester.place(x=10, y=350)
        self.sem = ttk.Combobox(self.fcontainer, font=("times new roman", 12, "bold"))
        self.sem["values"] = ("1st", "2nd","3rd","4th","5th","6th","7th","8th")
        self.sem.place(x=260, y=355, width=190)
        #====year======
        self.year = Label(self.fcontainer, text="Year:", font=("times new roman", 20, "bold"),
                              fg="yellow", bg="salmon")
        self.year.place(x=10, y=420)
        self.yr = ttk.Combobox(self.fcontainer, font=("times new roman", 12, "bold"))
        self.yr["values"] = ("1st year", "2nd year", "3rd year", "4th year")
        self.yr.place(x=260, y=425, width=190)
        #=======paid amount===
        self.paid = Label(self.fcontainer, text="Paid_Amount:", font=("times new roman", 20, "bold"),
                          fg="yellow", bg="salmon")
        self.paid.place(x=10, y=490)
        self.ent_paid = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                              relief=GROOVE, bg="lightgray")
        self.ent_paid.place(x=260, y=495)
        # ========due amount====
        self.due = Label(self.fcontainer, text="Due_Amount:", font=("times new roman", 20, "bold"),
                         fg="yellow", bg="salmon")
        self.due.place(x=10, y=560)
        self.ent_due = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                             relief=GROOVE, bg="lightgray")
        self.ent_due.place(x=260, y=565)
        # ====paid date========
        self.paid_date = Label(self.fcontainer, text="Paid_Date:", font=("times new roman", 20, "bold"),
                               fg="yellow", bg="salmon")
        self.paid_date.place(x=10, y=630)
        self.ent_paiddate = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                                  relief=GROOVE, bg="lightgray")
        self.ent_paiddate.place(x=260, y=635, width=190)
        # =======mode of payment========
        self.mode_pay = Label(self.fcontainer, text="Mode Of Payment:", font=("times new roman", 20, "bold"),
                              fg="yellow", bg="salmon")
        self.mode_pay.place(x=10, y=695)
        self.modepay = ttk.Combobox(self.fcontainer, font=("times new roman", 12, "bold"))
        self.modepay["values"] = ("Cash", "Cheque")
        self.modepay.place(x=260, y=700, width=188)
        # ======all buttons here=====
        self.btn_add = Button(self.fcontainer, text="ADD", font=("times new roman", 17, "bold"), bg="#2C3E4C",
                              fg="yellow", command=self.add).place(x=20, y=750, width=90)
        # ========update button====
        self.btn_update = Button(self.fcontainer, text="UPDATE", font=("times new roman", 17, "bold"),
                                 bg="#2C3E4C",
                                 fg="yellow", command=self.update).place(x=140, y=750, width=130)
        # =====delete=====
        self.btn_delete = Button(self.fcontainer, text="DELETE", font=("times new roman", 17, "bold"),
                                 bg="#2C3E4C",
                                 fg="yellow", command=self.delete).place(x=300, y=750, width=130)
        # =========clear========
        self.btn_clear = Button(self.fcontainer, text="CLEAR", font=("times new roman", 17, "bold"), bg="#2C3E4C",
                                fg="yellow", command=self.clear).place(x=460, y=750, width=90)

        scroll_x = Scrollbar(self.fourthcontainer, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.fourthcontainer, orient=VERTICAL)
        self.fee_table = ttk.Treeview(self.fourthcontainer, columns=("StudentID_N",
                                                                     "First Name", "Last Name"),
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.fee_table.xview)
        scroll_y.config(command=self.fee_table.yview)
        self.fee_table.heading("StudentID_No", text="Student ID_No")
        self.fee_table.heading("First Name", text="First  Name")
        self.fee_table.heading("Last Name", text="Last  Name")
        self.fee_table['show'] = "headings"
        self.fee_table.pack(fill=BOTH, expand=1)
        self.fee_table.bind("<ButtonRelease-1>", self.showdata_into_entry)

    def view_window(self):
        self.screen = Toplevel()
        self.screen.geometry("825x723+680+90")
        self.screen.config(bg="light blue")
        self.view_frame = Frame(self.screen, bd=5, bg="white", relief=RIDGE)
        self.view_frame.place(x=10, y=130, width=805, height=580)
        # ========searching======
        lbl_search = Label(self.screen, text="Search By:", font=("times new roman", 25, "bold"), fg="maroon",
                           bg="light blue")
        lbl_search.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.combo_search = ttk.Combobox(self.screen, width=13,
                                         font=("times new roman", 13, "bold"), state="readonly")
        self.combo_search["values"] = ("First_Name")
        self.combo_search.grid(row=0, column=1, padx=10, pady=10)
        self.search_ent = Entry(self.screen, font=("arial", 12, "bold"), bd=1, relief=GROOVE)
        self.search_ent.grid(row=0, column=2, padx=10, pady=10)
        search_btn = Button(self.screen, text="Search", font=("times new roman", 15, "bold"), bd=5, fg="black",
                            bg="white",
                            width=8, command=self.search_data1)
        search_btn.grid(row=0, column=3, padx=10, pady=10)
        searchall_btn = Button(self.screen, text="Search All", font=("times new roman", 15, "bold"), bd=5,
                               fg="black",
                               bg="white",
                               width=8, command=self.show_table)
        searchall_btn.grid(row=0, column=4, padx=10, pady=10)
        # =======sorting==========
        lbl_sort = Label(self.screen, text="Sort By:", font=("times new roman", 25, "bold"), fg="black",
                         bg="light blue")
        lbl_sort.place(x=10, y=70)
        combo_sort = ttk.Combobox(self.screen, width=13,
                                  font=("times new roman", 13, "bold"), state="readonly")
        combo_sort["values"] = ("Student_ID_No")
        combo_sort.place(x=140, y=76, width=200)
        sort_btn = Button(self.screen, text="Sort", font=("times new roman", 15, "bold"), bd=5, fg="black",
                          bg="yellow",
                          width=8, command=self.sorting)
        sort_btn.place(x=380, y=70)
        # =======scrollbar=======
        scroll_x = Scrollbar(self.view_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.view_frame, orient=VERTICAL)
        self.fees_table = ttk.Treeview(self.view_frame, columns=("Student_ID_No",
                                                                 "First_Name", "Last_Name", "Total Fees", "Semester",
                                                                 "Year", "Paid_Amount", "Due_amount", "Paid_Date",
                                                                 "Mode of Payment"),
                                       xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.fees_table.xview)
        scroll_y.config(command=self.fees_table.yview)
        self.fees_table.heading("Student_ID_No", text="Student_ID_No")
        self.fees_table.heading("First_Name", text="First_Name")
        self.fees_table.heading("Last_Name", text="Last_Name")
        self.fees_table.heading("Total Fees", text="Total Fees")
        self.fees_table.heading("Semester", text="Semester")
        self.fees_table.heading("Year", text="Year")
        self.fees_table.heading("Paid_Amount", text="Paid_Amount")
        self.fees_table.heading("Due_amount", text="Due_amount")
        self.fees_table.heading("Paid_Date", text="Paid_Date")
        self.fees_table.heading("Mode of Payment", text="Mode of Payment")
        self.fees_table['show'] = "headings"
        self.fees_table.pack(fill=BOTH, expand=1)
        self.show_table()
        self.fees_table.bind("<ButtonRelease-1>", self.displaydata_into_entry)

    def search_data(self):
        try:
            query = "select ID_No,First_Name,Last_Name from tbl_student where " + str(
                self.combo_search1.get()) + "=" + str(self.search_ent1.get())
            row = self.con_fee.select1(query)
            if len(row) != 0:
                self.fee_table.delete(*self.fee_table.get_children())
                for i in row:
                    self.fee_table.insert('', END, values=i)


        except Exception as es:

            messagebox.showerror("error", f"error due to {str(es)}")

    def showdata_into_entry(self, ev):
        row_cursor = self.fee_table.focus()
        contents = self.fee_table.item(row_cursor)
        row = contents['values']
        self.ent_id.delete(0, END)
        self.ent_id.insert(END, row[0])
        self.ent_Name.delete(0, END)
        self.ent_Name.insert(END, row[1])
        self.ent_lname.delete(0, END)
        self.ent_lname.insert(END, row[2])

    def add(self):
        if self.ent_id.get() == "" or self.ent_Name.get() == "" or self.ent_lname.get() == "" or self.ent_fee.get() == "" or \
                self.sem.get() == "" or self.yr.get() == "" or self.ent_paid.get() == "" or self.ent_due.get() == "" or \
                self.ent_paiddate.get() == "" or self.modepay.get() == "":
            messagebox.showerror("Error", "All fields are required")

        elif self.ent_Name.get().isdigit() or self.ent_lname.get().isdigit():
            messagebox.showerror("error", "integer value is not allowed in first name ,last name and answer")
        else:
            try:

                fee_obj = Model_fee(self.ent_id.get(), self.ent_Name.get(), self.ent_lname.get(), self.ent_fee.get(),
                                    self.sem.get(), self.yr.get(), self.ent_paid.get(), self.ent_due.get(),
                                    self.ent_paiddate.get(),
                                    self.modepay.get())
                query = "insert into tbl_fee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
                values = (fee_obj.get_ID_No(), fee_obj.get_First_Name(), fee_obj.get_Last_Name(),
                          fee_obj.get_Total_fees(), fee_obj.get_semester(), fee_obj.get_year(),
                          fee_obj.get_Paid_amount(),
                          fee_obj.get_Due_amount(), fee_obj.get_Paid_date(), fee_obj.get_Modeof_payment())
                self.con_fee.insert(query, values)
                messagebox.showinfo("error", "Data inserted in database successfully")
                self.clear()


            except Exception as e:
                messagebox.showerror("error", f"error due to {str(e)}")

    def show_table(self):
        query_select = "select * from tbl_fee;"
        row1 = self.con_fee.select1(query_select)
        if len(row1) != 0:
            self.fees_table.delete(*self.fees_table.get_children())
            for i in row1:
                self.fees_table.insert('', END, values=i)

    def clear(self):
        self.ent_id.delete(0, END)
        self.ent_Name.delete(0, END)
        self.ent_lname.delete(0, END)
        self.ent_fee.delete(0, END)
        self.sem.delete(0, END)
        self.yr.delete(0, END)
        self.ent_paid.delete(0, END)
        self.ent_due.delete(0, END)
        self.ent_paiddate.delete(0, END)
        self.modepay.delete(0, END)

    def displaydata_into_entry(self, ev):
        row_cursor = self.fees_table.focus()
        contents = self.fees_table.item(row_cursor)
        row = contents['values']
        self.ent_id.delete(0, END)
        self.ent_id.insert(END, row[0])
        self.ent_Name.delete(0, END)
        self.ent_Name.insert(END, row[1])
        self.ent_lname.delete(0, END)
        self.ent_lname.insert(END, row[2])
        self.ent_fee.delete(0, END)
        self.ent_fee.insert(END, row[3])
        self.sem.delete(0, END)
        self.sem.insert(END, row[4])
        self.yr.delete(0, END)
        self.yr.insert(END, row[5])
        self.ent_paid.delete(0, END)
        self.ent_paid.insert(END, row[6])
        self.ent_due.delete(0, END)
        self.ent_due.insert(END, row[7])
        self.ent_paiddate.delete(0, END)
        self.ent_paiddate.insert(END, row[8])
        self.modepay.delete(0, END)
        self.modepay.insert(END, row[9])

    def delete(self):
        if self.ent_id.get() == "":
            messagebox.showerror("error", "please enter id nnumber to delete")
        else:

            try:
                query = "delete from tbl_fee where Student_ID_No=%s;"
                fee_obj = Model_fee(self.ent_id.get(), self.ent_Name.get(), self.ent_lname.get(),
                                    self.ent_fee.get(), self.sem.get(), self.yr.get(), self.ent_paid.get(),
                                    self.ent_due.get(), self.ent_paiddate.get(), self.modepay.get())
                value = (fee_obj.get_ID_No(),)
                self.con_fee.delete(query, value)
                messagebox.showinfo("success", "data deleted successfully")
                self.show_table()
                self.clear()

            except Exception as es:
                messagebox.showerror("error", f"error due to {str(es)} ")

    def update(self):
        if self.ent_id.get() == "":
            messagebox.showerror("error", "please enter the student id to update student data")
        else:
            try:
                fee_obj = Model_fee(self.ent_id.get(), self.ent_Name.get(), self.ent_lname.get(),
                                    self.ent_fee.get(), self.sem.get(), self.yr.get(), self.ent_paid.get(),
                                    self.ent_due.get(), self.ent_paiddate.get(), self.modepay.get())
                query = "update tbl_fee set Total_Fees=%s,Semester=%s,Year=%s,Paid_Amount=%s,Due_Amount=%s," \
                        "Paid_Date=%s,Mode_Of_Payment=%s where Student_ID_No=%s;"
                values = (
                    fee_obj.get_Total_fees(), fee_obj.get_semester(), fee_obj.get_year(),
                    fee_obj.get_Paid_amount(), fee_obj.get_Due_amount(), fee_obj.get_Paid_date(),
                    fee_obj.get_Modeof_payment(), fee_obj.get_ID_No())
                self.con_fee.update(query, values)
                messagebox.showinfo("success", "Data updated successfully")
                self.show_table()
                self.clear()


            except Exception as es:
                messagebox.showerror("error", f"error due to {str(es)} ")

    def sorting(self):
        query = "select * from tbl_fee;"
        records = self.con_fee.select1(query)
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
            self.fees_table.delete(*self.fees_table.get_children())
            for i in list:
                self.fees_table.insert('', END, values=i)

    def search_data1(self):
        query = "select First_Name from tbl_fee;"
        records = self.con_fee.select1(query)
        data_list = []
        for row in records:
            data_list.append(row[0])
        ans = self.linear_search(data_list, self.search_ent.get())

    def linear_search(self, data, item):
        for i in data:
            if i == item:
                messagebox.showinfo('Success', 'congrats Name exists in this list', parent=self.screen)
                query1 = "select * from tbl_fee where First_Name=%s;"
                values1 = (self.search_ent.get(),)
                records1 = self.con_fee.select(query1, values1)
                if len(records1) != 0:
                    self.fees_table.delete(*self.fees_table.get_children())
                    for i in records1:
                        self.fees_table.insert('', END, values=i)

                break
        else:
            messagebox.showerror('error', 'sorry this Name doesnot exist in this list', parent=self.screen)

    # window=Tk()
    # Fees(window)
    # window.mainloop()