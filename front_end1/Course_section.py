from tkinter import*
from tkinter import ttk
from model_class1.course_model import*
from back_end1.register_connection import*
from tkinter import messagebox
class Course:
    def __init__(self,screen):
        self.wn1=screen
        self.wn1.geometry("1480x830+50+0")
        self.wn1.title("Course management".center(450))
        self.wn1.configure(background="tomato")
        #==========database connection======
        self.con_course=register_database()
        # ======third frame=========
        self.container_4 = Frame(self.wn1, bg="limegreen", bd=10, relief=RIDGE)
        self.container_4.place(x=10, y=90, width=500, height=730)
        self.head5 = Label(self.wn1, text="COURSE", font=("times new roman", 40, "bold"), bg="tomato",
                           fg="black")
        self.head5.place(x=700, y=10)
        self.head4 = Label(self.container_4, text=" Course Details", font=("times new roman", 20, "bold"),bg="limegreen",
                           fg="white")
        self.head4.place(x=190,y=30)
        #====courseID=====
        self.course_ID = Label(self.container_4, text="Course_ID:", font=("times new roman", 20, "bold"),
                            fg="white", bg="limegreen").place(x=100, y=100)
        self.ent_course_ID = Entry(self.container_4, font=("arial", 12, "bold"), bd=1, relief=GROOVE,
                                bg="lightgray")
        self.ent_course_ID.place(x=100, y=150)
        #===course name=====
        self.course_name = Label(self.container_4, text="Course_Name:", font=("times new roman", 20, "bold"),
                               fg="white", bg="limegreen").place(x=100, y=200)

        self.combobox2=ttk.Combobox(self.container_4,font=("arial",15,"bold"))
        self.combobox2["values"]=("cloud","Bsc(computing system)","Ethical hacking and security","MBA","BBA","BIT","BIM","CA")
        self.combobox2.place(x=100,y=250,width=300)
        #======course desciption====
        self.course_desc = Label(self.container_4, text="Course_Description:", font=("times new roman", 20, "bold"),
                                 fg="white", bg="limegreen").place(x=100, y=300)

        self.course_textbox=Text(self.container_4,font=("arial",15,"bold"),bg="lightgray")
        self.course_textbox.place(x=100,y=350,width=260,height=100)
        self.total_yr = Label(self.container_4, text="Total Year:", font=("times new roman", 20, "bold"),
                                 fg="white", bg="limegreen").place(x=100, y=465)
        self.ent_total_yr= Entry(self.container_4, font=("arial", 12, "bold"), bd=1, relief=GROOVE,
                                   bg="lightgray")
        self.ent_total_yr.place(x=100, y=505)

        #=====save button=====
        self.btn_add1 = Button(self.container_4, text="SAVE", font=("times new roman", 17, "bold"), bg="#2C3E4C",
                              fg="yellow",cursor="hand2",command=self.add).place(x=100, y=620, width=90)

        self.btn_delete = Button(self.container_4, text="DELETE", font=("times new roman", 17, "bold"), bg="#2C3E4C",
                              fg="yellow",cursor="hand2",command=self.delete).place(x=200, y=620, width=100)
        self.btn_clear = Button(self.container_4, text="CLEAR", font=("times new roman", 17, "bold"), bg="#2C3E4C",
                                 fg="yellow",cursor="hand2",command=self.clear).place(x=320, y=620, width=100)
        self.container_5 = Frame(self.wn1, bg="limegreen", bd=10, relief=RIDGE)
        self.container_5.place(x=530, y=90, width=930, height=730)
        self.container_6 = Frame(self.container_5, bg="white", bd=4, relief=RIDGE)
        self.container_6.place(x=15, y=120, width=880, height=580)
        #==========sorting
        # =======sorting==========
        lbl_sort = Label(self.container_5, text="Sort By:", font=("times new roman", 20, "bold"), fg="yellow",
                         bg="limegreen")
        lbl_sort.place(x=10, y=70)
        combo_sort = ttk.Combobox(self.container_5, width=13,
                                  font=("times new roman", 13, "bold"), state="readonly")
        combo_sort["values"] = ("Course_name")
        combo_sort.place(x=140, y=76, width=200)
        sort_btn = Button(self.container_5, text="Sort", font=("times new roman", 15, "bold"), bd=5, fg="black",
                          bg="yellow",cursor="hand2",
                          width=8,command=self.sorting)
        sort_btn.place(x=380, y=70)
        #=====searching===
        lbl_search = Label(self.container_5, text="Search By:", font=("times new roman", 25, "bold"), fg="white",
                           bg="limegreen")
        lbl_search.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.combo_search = ttk.Combobox(self.container_5, width=13,
                                    font=("times new roman", 13, "bold"), state="readonly")
        self.combo_search["values"] = ("Course_name")
        self.combo_search.grid(row=0, column=1, padx=10, pady=10)
        self.search_ent = Entry(self.container_5, font=("arial", 12, "bold"), bd=1, relief=GROOVE)
        self.search_ent.grid(row=0, column=2, padx=10, pady=10)
        search_btn = Button(self.container_5, text="Search", font=("times new roman", 15, "bold"), bd=5, fg="black",
                            bg="white",cursor="hand2",
                            width=8,command=self.search_data)
        search_btn.grid(row=0, column=3, padx=10, pady=10)
        searchall_btn = Button(self.container_5, text="Search All", font=("times new roman", 15, "bold"), bd=5,
                               fg="black",
                               bg="white",cursor="hand2",
                               width=8,command=self.show_table)
        searchall_btn.grid(row=0, column=4, padx=10, pady=10)
        scroll_x = Scrollbar(self.container_6, orient=HORIZONTAL)
        scroll_y = Scrollbar(self.container_6, orient=VERTICAL)
        self.course_table = ttk.Treeview(self.container_6, columns=(
        "Course_ID","Course_Name","Course_description","Total_year"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.course_table.xview)
        scroll_y.config(command=self.course_table.yview)
        self.course_table.heading("Course_ID", text="Course_ID")
        self.course_table.heading("Course_Name", text="Course_Name")
        self.course_table.heading("Course_description", text="Course_description")
        self.course_table.heading("Total_year", text="Total_year")
        self.course_table['show']="headings"
        self.course_table.pack(fill=BOTH,expand=1)
        self.show_table()
        self.course_table.bind("<ButtonRelease-1>",self.show_data_entry)

    def add(self):
        if self.ent_course_ID.get()==""or self.combobox2.get()==""or self.course_textbox.get('1.0',END)==""or self.ent_total_yr.get()=="":
            messagebox.showerror("error","all fields are required")

        elif self.ent_course_ID.get().isalpha() or self.ent_total_yr.get().isalpha():
            messagebox.showerror("Error","string value isnot  allowed in course id and total year ")


        else:

            try:

                course_mod=Model_course(self.ent_course_ID.get(),self.combobox2.get(),self.course_textbox.get('1.0',END),self.ent_total_yr.get())
                query="insert into tbl_course values(%s,%s,%s,%s);"
                values=(course_mod.get_course_id(),course_mod.get_course_name(),course_mod.get_course_description(),course_mod.get_total_year())
                self.con_course.insert(query,values)
                messagebox.showinfo("success","Data inserted successfully")
                self.show_table()
                self.clear()

            except Exception as es:
                messagebox.showerror("error",f"error due to {str(es)}")


    def clear(self):
        self.ent_course_ID.delete(0,END)
        self.ent_total_yr.delete(0,END)
        self.course_textbox.delete(1.0,END)
        self.combobox2.delete(0,END)


    def show_table(self):
        query_select="select * from tbl_course;"
        row1=self.con_course.select1(query_select)
        if len(row1)!=0:
            self.course_table.delete(*self.course_table.get_children())
            for i in row1:
                self.course_table.insert('',END,values=i)


    def show_data_entry(self,ev):
        row_cursor=self.course_table.focus()
        contents=self.course_table.item(row_cursor)
        row=contents['values']
        self.ent_course_ID.delete(0,END)
        self.ent_course_ID.insert(END,row[0])
        self.combobox2.delete(0,END)
        self.combobox2.insert(END,row[1])
        self.course_textbox.delete('1.0',END)
        self.course_textbox.insert(END,row[2])
        self.ent_total_yr.delete(0,END)
        self.ent_total_yr.insert(END,row[3])

    def delete(self):
        if self.ent_course_ID.get()=="":
            messagebox.showerror("error","please enter the course id to delete that particular course")
        else:
            try:
                query="delete from tbl_course where Course_ID=%s;"
                course_mod=Model_course(int(self.ent_course_ID.get()),self.combobox2.get(),self.course_textbox.get('1.0',END),
                                        int(self.ent_total_yr.get()))
                value=(course_mod.get_course_id(),)
                self.con_course.delete(query,value)
                messagebox.showinfo("success","data deleted successfully")
                self.show_table()
                self.clear()

            except Exception as es:
                messagebox.showerror("error",f"error due to {str(es)} ")

    def search_data(self):
        query = "select Course_name from tbl_course;"
        records = self.con_course.select1(query)
        data_list = []
        for row in records:
            data_list.append(row[0])
        ans = self.linear_search(data_list, self.search_ent.get())

    @classmethod
    def linear_search(self, data, item):
        for i in data:
            if i == item:
                messagebox.showinfo('Success', 'congrats this course exists in this list')
                # query1 = "select * from tbl_course where Course_name=%s;"
                # values1 = (self.search_ent.get(),)
                # records1 = self.con_course.select(query1, values1)
                # if len(records1)!=0:
                #     self.course_table.delete(*self.course_table.get_children())
                #     for i in records1:
                #         self.course_table.insert("",END,values=i)

                break

        else:
            messagebox.showerror('error', 'sorry this course name doesnot exist in this list')

    def sorting(self):
        query = "select Course_name from tbl_course;"
        records = self.con_course.select1(query)
        data_list1 = []
        for row in records:
            data_list1.append(row)
        d = self.bubblesort_ascending(data_list1)

    @classmethod
    def bubblesort_ascending(self, list):
        for j in range(len(list) - 1):
            for i in range(len(list) - 1):
                if list[i] > list[i + 1]:
                    list[i], list[i + 1] = list[i + 1], list[i]
        messagebox.showinfo("success","The Course name has been sorted in ascending order.")
        # if len(list) != 0:
        #     self.course_table.delete(*self.course_table.get_children())
        #     for i in list:
        #         self.course_table.insert('', END, values=i)



# window=Tk()
# Course(window)
# window.mainloop()