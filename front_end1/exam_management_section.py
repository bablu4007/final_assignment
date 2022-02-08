from tkinter import*
from tkinter import ttk
from model_class1.exam_model import*
from tkinter import  messagebox
from back_end1.register_connection import*

class Exam:
    def __init__(self,screen):
        self.wn=screen
        self.wn.geometry("1480x830+50+0")
        self.wn.title("Exam management".center(480))
        self.wn.config(background="#00FF00")
        self.con_exam=register_database()
        # ======first frame=========
        self.fcontainer = Frame(self.wn, bg="#660066", bd=10, relief=RIDGE)
        self.fcontainer.place(x=10, y=50, width=600, height=780)
        self.head2 = Label(self.fcontainer, text=" Result Details", font=("times new roman", 25, "bold"),
                           bg="#660066", fg="white")
        self.head2.pack(side=TOP)
        # =====heading=======
        self.head1 = Label(self.wn, text="RESULTS  DATA", font=("times new roman", 30, "bold"), bg="#00FF00",
                           fg="black")
        self.head1.place(x=700, y=0)
        # =======second container========
        self.scontainer = Frame(self.wn, bg="#660066", bd=10, relief=RIDGE)
        self.scontainer.place(x=620, y=50, width=850, height=780)
        # =====third frame========
        self.tcontainer = Frame(self.scontainer, bg="light blue", bd=2, relief=GROOVE)
        self.tcontainer.place(x=0, y=0, width=827, height=50)

        # ====button for viewing all data=========
        self.view_btn = Button(self.tcontainer, text="View All Data", font=("arial", 15, "bold"), bd=5,
                               bg="yellow", command=self.view_window)
        self.view_btn.place(x=300, y=3, width=200, height=40)

        #====searching=========
        lbl_search = Label(self.scontainer, text="Search By:", font=("times new roman", 25, "bold"), fg="yellow",
                           bg="#660066")
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
                        fg="yellow", bg="#660066")
        self.id.place(x=10, y=70)
        self.ent_id = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                            relief=GROOVE, bg="lightgray")
        self.ent_id.place(x=260, y=75)
        # ======first name======
        self.firstname = Label(self.fcontainer, text="First_Name:", font=("times new roman", 20, "bold"),
                               fg="yellow", bg="#660066")
        self.firstname.place(x=10, y=140)
        self.ent_Name = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                              relief=GROOVE, bg="lightgray")
        self.ent_Name.place(x=260, y=145)
        # ===last name======
        self.lastname = Label(self.fcontainer, text="Last_Name:", font=("times new roman", 20, "bold"),
                              fg="yellow", bg="#660066")
        self.lastname.place(x=10, y=210)
        self.ent_lname = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                               relief=GROOVE, bg="lightgray")
        self.ent_lname.place(x=260, y=215)
        # ====marks obtained=========
        self.obtainmrk = Label(self.fcontainer, text="Marks Obtained:", font=("times new roman", 20, "bold"),
                         fg="yellow", bg="#660066")
        self.obtainmrk.place(x=10, y=280)
        self.ent_markobtain = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                             relief=GROOVE, bg="lightgray")
        self.ent_markobtain.place(x=260, y=285)
        # ======total marks=====
        self.totalmark = Label(self.fcontainer, text="Total Marks:", font=("times new roman", 20, "bold"),
                              fg="yellow", bg="#660066")
        self.totalmark.place(x=10, y=350)
        self.ent_totalmark = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                             relief=GROOVE, bg="lightgray")
        self.ent_totalmark.place(x=260, y=355)
        # ====percentage======
        self.percent = Label(self.fcontainer, text="Percentage:", font=("times new roman", 20, "bold"),
                          fg="yellow", bg="#660066")
        self.percent.place(x=10, y=420)
        self.ent_percentage = Entry(self.fcontainer, font=("arial", 12, "bold"), bd=1,
                                   relief=GROOVE, bg="lightgray")
        self.ent_percentage.place(x=260, y=425)


        # ======all buttons here=====
        self.btn_add = Button(self.fcontainer, text="ADD", font=("times new roman", 17, "bold"), bg="#2C3E4C",
                              fg="yellow",command=self.add).place(x=20, y=600, width=90)
        # ========update button====
        self.btn_update = Button(self.fcontainer, text="UPDATE", font=("times new roman", 17, "bold"),
                                 bg="#2C3E4C",
                                 fg="yellow",command=self.update).place(x=140, y=600, width=130)
        # =====delete=====
        self.btn_delete = Button(self.fcontainer, text="DELETE", font=("times new roman", 17, "bold"),
                                 bg="#2C3E4C",
                                 fg="yellow",command=self.delete).place(x=300, y=600, width=130)
        # =========clear========
        self.btn_clear = Button(self.fcontainer, text="CLEAR", font=("times new roman", 17, "bold"), bg="#2C3E4C",
                                fg="yellow",command=self.clear).place(x=460, y=600, width=90)

        scroll_x = Scrollbar(self.fourthcontainer, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.fourthcontainer, orient=VERTICAL)
        self.exam_table1 = ttk.Treeview(self.fourthcontainer, columns=("Student_ID_No",
                                                                     "First_Name", "Last_Name"),
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.exam_table1.xview)
        scroll_y.config(command=self.exam_table1.yview)
        self.exam_table1.heading("Student_ID_No", text="Student_ID_No")
        self.exam_table1.heading("First_Name", text="First_Name")
        self.exam_table1.heading("Last_Name", text="Last_Name")
        self.exam_table1['show'] = "headings"
        self.exam_table1.pack(fill=BOTH, expand=1)
        self.exam_table1.bind("<ButtonRelease-1>", self.showdata_into_entry)

    def view_window(self):
        self.screen = Toplevel()
        self.screen.geometry("825x723+680+90")
        self.screen.config(bg="light green")
        # =====first frame inside view window=======
        self.view_frame = Frame(self.screen, bd=5, bg="white", relief=RIDGE)
        self.view_frame.place(x=10,y=130,width=805,height=580)
        # ========searching======
        lbl_search = Label(self.screen, text="Search By:", font=("times new roman", 25, "bold"), fg="maroon",
                           bg="light green")
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
        scroll_x = Scrollbar(self.view_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.view_frame, orient=VERTICAL)
        self.exam_table = ttk.Treeview(self.view_frame, columns=("Student_ID_No",
                                                                "First_Name", "Last_Name", "Marks_Obtained", "Total_Marks",
                                                                "Percentage"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)



        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.exam_table.xview)
        scroll_y.config(command=self.exam_table.yview)
        self.exam_table.heading("Student_ID_No", text="Student_ID_No")
        self.exam_table.heading("First_Name", text="First_Name")
        self.exam_table.heading("Last_Name", text="Last_Name")
        self.exam_table.heading("Marks_Obtained", text="Marks_Obtained")
        self.exam_table.heading("Total_Marks", text="Total_Marks")
        self.exam_table.heading("Percentage", text="Percentage")
        self.exam_table['show'] = "headings"
        self.exam_table.pack(fill=BOTH, expand=1)
        self.show_table()
        self.exam_table.bind("<ButtonRelease-1>", self.displaydata_into_entry)

    def search_data(self):
        try:
            query = "select ID_No,First_Name,Last_Name from tbl_student where " + str(
                self.combo_search1.get()) + "=" + str(self.search_ent1.get())
            row = self.con_exam.select1(query)
            # print(row)
            if len(row) != 0:
                self.exam_table1.delete(*self.exam_table1.get_children())
                for i in row:
                    self.exam_table1.insert('', END, values=i)


        except Exception as es:

            messagebox.showerror("error",f"error due to {str(es)}")


    def showdata_into_entry(self,ev):
        row_cursor=self.exam_table1.focus()
        contents=self.exam_table1.item(row_cursor)
        row=contents['values']
        self.ent_id.delete(0, END)
        self.ent_id.insert(END,row[0])
        self.ent_Name.delete(0, END)
        self.ent_Name.insert(END,row[1])
        self.ent_lname.delete(0, END)
        self.ent_lname.insert(END,row[2])

    def add(self):
        if self.ent_id.get()=="" or self.ent_Name.get()=="" or self.ent_lname.get()=="" or \
                self.ent_markobtain.get()=="" or self.ent_totalmark.get()=="" or self.ent_percentage.get()=="":
            messagebox.showerror("Error","All fields are required")

        elif self.ent_Name.get().isdigit() or self.ent_lname.get().isdigit():
            messagebox.showerror("error", "integer value is not allowed in first name ,last name ")
        elif self.ent_id.get().isalpha() or self.ent_markobtain.get().isalpha() or \
                self.ent_totalmark.get().isalpha() or self.ent_percentage.get().isalpha():
            messagebox.showerror("Error", "Alphabetical value is not allowed in student id,marks obtain,total marks and percentage")
        else:
            try:

                exam_obj=Model_exam(self.ent_id.get(),self.ent_Name.get(),self.ent_lname.get(),
                                    self.ent_markobtain.get(),self.ent_totalmark.get(),self.ent_percentage.get())
                query="insert into tbl_exam values(%s,%s,%s,%s,%s,%s);"
                values=(exam_obj.get_ID(),exam_obj.get_first_name(),exam_obj.get_last_name(),
                        exam_obj.get_marks_obtain(),exam_obj.get_total_marks(),exam_obj.get_percentage())
                self.con_exam.insert(query,values)
                messagebox.showinfo("error","Data inserted in database successfully")
                self.clear()


            except Exception as e:
                messagebox.showerror("error",f"error due to {str(e)}")


    def show_table(self):
        query_select="select * from tbl_exam;"
        row1=self.con_exam.select1(query_select)
        if len(row1)!=0:
            self.exam_table.delete(*self.exam_table.get_children())
            for i in row1:
                self.exam_table.insert('',END,values=i)

    def clear(self):
        self.ent_id.delete(0,END)
        self.ent_Name.delete(0, END)
        self.ent_lname.delete(0, END)
        self.ent_markobtain.delete(0, END)
        self.ent_totalmark.delete(0, END)
        self.ent_percentage.delete(0, END)

    def displaydata_into_entry(self,ev):
        row_cursor=self.exam_table.focus()
        contents=self.exam_table.item(row_cursor)
        row=contents['values']
        self.ent_id.delete(0, END)
        self.ent_id.insert(END, row[0])
        self.ent_Name.delete(0, END)
        self.ent_Name.insert(END, row[1])
        self.ent_lname.delete(0, END)
        self.ent_lname.insert(END, row[2])
        self.ent_markobtain.delete(0, END)
        self.ent_markobtain.insert(END,row[3])
        self.ent_totalmark.delete(0, END)
        self.ent_totalmark.insert(END, row[4])
        self.ent_percentage.delete(0, END)
        self.ent_percentage.insert(END, row[5])

    def delete(self):
        if self.ent_id.get() == "":
            messagebox.showerror("error", "please enter id nnumber to delete")
        else:

            try:
                query = "delete from tbl_exam where Student_ID_No=%s;"
                exam_obj=Model_exam(self.ent_id.get(),self.ent_Name.get(),self.ent_lname.get(),
                                    self.ent_markobtain.get(),self.ent_totalmark.get(),self.ent_percentage.get())
                value = (exam_obj.get_ID(),)
                self.con_exam.delete(query, value)
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
                exam_obj=Model_exam(self.ent_id.get(),self.ent_Name.get(),self.ent_lname.get(),
                                    self.ent_markobtain.get(),self.ent_totalmark.get(),self.ent_percentage.get())
                query = "update tbl_exam set Marks_obtained=%s,Total_Marks=%s,Percentage=%s where Student_ID_No=%s;"
                values = (
                    exam_obj.get_marks_obtain(),exam_obj.get_total_marks(),exam_obj.get_percentage(),exam_obj.get_ID())
                self.con_exam.update(query, values)
                messagebox.showinfo("success", "Data updated successfully",parent=self.screen)
                self.show_table()
                self.clear()


            except Exception as es:
                messagebox.showerror("error", f"error due to {str(es)} ")
    def sorting(self):
        query = "select * from tbl_exam;"
        records = self.con_exam.select1(query)
        data_list1 = []
        for row in records:
            data_list1.append(row)
        d = self.bubblesort_ascending(data_list1)

    def bubblesort_ascending(self, list):
        for j in range(len(list) - 1):
            for i in range(len(list) - 1):
                if list[i] > list[i + 1]:
                    list[i], list[i + 1] = list[i + 1], list[i]
        messagebox.showinfo("success","list has been sorted by student id number in ascending order.")
        if len(list) != 0:
            self.exam_table.delete(*self.exam_table.get_children())
            for i in list:
                self.exam_table.insert('', END, values=i)

    def search_data1(self):
        query = "select First_Name from tbl_exam;"
        records = self.con_exam.select1(query)
        data_list = []
        for row in records:
            data_list.append(row[0])
        ans = self.linear_search(data_list, self.search_ent.get())

    def linear_search(self, data, item):
        for i in data:
            if i == item:
                messagebox.showinfo('Success', 'congrats Name exists in this list',parent=self.screen)
                query1 ="select * from tbl_exam where First_Name=%s;"
                values1=(self.search_ent.get(),)
                records1 = self.con_exam.select(query1,values1)
                if len(records1) != 0:
                    self.exam_table.delete(*self.exam_table.get_children())
                    for row in records1:
                        self.exam_table.insert('', END, values=row)
                break
        else:
            messagebox.showerror('error', 'sorry this Name doesnot exist in this list',prent=self.screen)




# window=Tk()
# Exam(window)
# window.mainloop()