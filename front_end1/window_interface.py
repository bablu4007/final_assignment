from tkinter import*
from front_end1.exam_management_section import*
from front_end1.staff_management_section import*
from front_end1.fees_management_section import*
from front_end1.Student_attendance_section import*
from front_end1.staff_attendance_section import*
from front_end1.Course_section import*
from front_end1.student_management_section import*
from tkcalendar import *
from tkinter import ttk
class Mainwindow:
    def __init__(self,screen):
        self.wn=screen
        self.wn.geometry("1480x830+50+0")
        self.wn.title("University management system".center(460))
        self.wn.configure(background="orange")
        self.wn.resizable(0, 0)
        # ===========heading==========
        self.heading = Label(self.wn, text="University Management System", bd=2, relief=GROOVE,
                        font=("times new roman", 30, "bold"), fg="yellow", bg="crimson")
        self.heading.pack(side=TOP, fill=X)
        # ======first frame=========
        self.container_first = Frame(self.wn, bg="#2C3E4C", bd=5, relief=RIDGE)
        self.container_first.place(x=60, y=50, width=1380, height=780)
        self.canvas_btn1 = Canvas(self.container_first, width=150, height=100)
        self.canvas_btn1.place(x=400, y=30)
        self.photo1 = PhotoImage(file="C:\\Users\Bablu\pythonProject\\final_assignment_semIII\\images\\book.jpg")
        self.canvas_btn1.create_image(0, 0, image=self.photo1, anchor=NW)
        # =======button1=====
        self.btn1 = Button(self.container_first, text="Course", font=("times new roman", 15, "bold"), bd=8,
                           relief=GROOVE, bg="light blue", cursor="hand2", command=self.course_window)
        self.btn1.place(x=580, y=50, width=210)
        # =======image1======
        self.canvas_btn2 = Canvas(self.container_first, width=150, height=100)
        self.canvas_btn2.place(x=400, y=180)
        self.photo2 = PhotoImage(file="C:\\Users\Bablu\pythonProject\\final_assignment_semIII\images\\teacher.png")
        self.canvas_btn2.create_image(0, 0, image=self.photo2, anchor=NW)
        # =======button2=====
        self.btn2 = Button(self.container_first, text="Staff Management", font=("times new roman", 15, "bold"), bd=8,
                           relief=GROOVE, bg="light blue", cursor="hand2", command=self.staff_window)
        self.btn2.place(x=580, y=200, width=210)
        # ===image2======
        self.canvas_btn3 = Canvas(self.container_first, width=150, height=100)
        self.canvas_btn3.place(x=400, y=340)
        self.photo3 = PhotoImage(file="C:\\Users\Bablu\pythonProject\\final_assignment_semIII\\images\\money.jpg")
        self.canvas_btn3.create_image(0, 0, image=self.photo3, anchor=NW)
        # =======button3=====
        self.btn3 = Button(self.container_first, text="Fees Management", font=("times new roman", 15, "bold"), bd=8,
                           relief=GROOVE, bg="light blue", cursor="hand2", command=self.fee_window)
        self.btn3.place(x=580, y=360, width=210)
        # =======button4=====
        self.canvas_btn4 = Canvas(self.container_first, width=150, height=100)
        self.canvas_btn4.place(x=400, y=490)
        self.photo4 = PhotoImage(file="C:\\Users\Bablu\pythonProject\\final_assignment_semIII\\images\\exam.png")
        self.canvas_btn4.create_image(0, 0, image=self.photo4, anchor=NW)
        self.btn4 = Button(self.container_first, text="Exam Management", font=("times new roman", 15, "bold"), bd=8,
                           relief=GROOVE, bg="light blue", cursor="hand2", command=self.exam_window)
        self.btn4.place(x=580, y=510, width=210)
        # =======button5=====
        self.canvas_btn5 = Canvas(self.container_first, width=150, height=100)
        self.canvas_btn5.place(x=400, y=650)
        self.photo5 = PhotoImage(file="C:\\Users\Bablu\\pythonProject\\final_assignment_semIII\\images\\attendance.png")
        self.canvas_btn5.create_image(0, 0, image=self.photo5, anchor=NW)
        self.btn5 = Button(self.container_first, text=" Student Attendance ", font=("times new roman", 15, "bold"),
                           bd=8,
                           relief=GROOVE, bg="light blue", cursor="hand2", command=self.Student_attendance_window)
        self.btn5.place(x=580, y=670, width=210)
        # ========button6=====
        self.canvas_btn6 = Canvas(self.container_first, width=150, height=100)
        self.canvas_btn6.place(x=900, y=200)
        self.photo6 = PhotoImage(file="C:\\Users\\Bablu\\pythonProject\\final_assignment_semIII\\images\\membership.png")
        self.canvas_btn6.create_image(0, 0, image=self.photo6, anchor=NW)
        self.btn6 = Button(self.container_first, text="Staff Attendance", font=("times new roman", 15, "bold"), bd=8,
                           relief=GROOVE, bg="light blue", cursor="hand2", command=self.Staff_attendance_window)
        self.btn6.place(x=1080, y=200, width=210)
        # ========button7=====
        self.canvas_btn7 = Canvas(self.container_first, width=150, height=100)
        self.canvas_btn7.place(x=900, y=400)
        self.photo7 = PhotoImage(file="C:\\Users\Bablu\pythonProject\\final_assignment_semIII\\images\\studenty (1).png")
        self.canvas_btn7.create_image(0, 0, image=self.photo7, anchor=NW)
        self.btn6 = Button(self.container_first, text="Student Management", font=("times new roman", 15, "bold"), bd=8,
                           relief=GROOVE, bg="light blue", cursor="hand2", command=self.student_window)
        self.btn6.place(x=1080, y=400, width=210)
        self.calc = Calendar(self.wn, selectmode="day", date_pattern="yyyy/mm/dd")
        self.calc.place(x=100, y=100)

    def exam_window(self):
        new_window = Tk()
        Exam(new_window)
    def staff_window(self):
        new_window = Tk()
        Staff(new_window)
    def fee_window(self):
        new_window = Tk()
        Fees(new_window)
    def Student_attendance_window(self):
        new_window = Tk()
        Attendance(new_window)
    def Staff_attendance_window(self):
        new_window = Tk()
        Staff_attendance(new_window)
    def course_window(self):
        new_window = Toplevel()
        Course(new_window)
    def student_window(self):
        new_window = Tk()
        Student(new_window)

# window=Tk()
# Mainwindow(window)
# window.mainloop()