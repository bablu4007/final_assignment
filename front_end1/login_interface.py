from tkinter import*
from front_end1.window_interface import*
from tkinter import ttk
from tkinter import messagebox
from back_end1.register_connection import*
# import binascii, hashlib
# from front_end1.register_interface import Register
class Login:
    def __init__(self,screen):
        self.wn=screen
        self.wn.geometry("1470x830+60+0")
        self.wn.title("Login window".center(400))
        self.wn.configure(background="teal")
        self.wn.resizable(0,0)
        self.con_login=register_database()

        #======frame=====
        self.frame2 = Frame(self.wn, bg="teal")
        self.frame2.place(x=10, y=50, width=530, height=440)
        #=======image=======
        self.canvas5 = Canvas(self.wn, width=1470, height=830)
        self.canvas5.place(x=544, y=70)
        self.photo = PhotoImage(file="C:\\Users\\Bablu\\pythonProject\\final_assignment_semIII\\images\\login_bg.png.")
        self.canvas5.create_image(0, 0, image=self.photo, anchor=NW)
        self.uni=Label(self.wn,text="University",font=("times new roman",30,"bold"),bg="#2C3E4C",fg="darkturquoise")
        self.uni.place(x=900,y=20)
        #=====label=====
        self.lbl1=Label(self.frame2,text="Login Here",font=("impact",35,"bold"),bg="teal",fg="skyblue").place(x=40,y=10)
        self.lbl2 =Label(self.frame2, text="Admin Login Area", font=("Goudy old style", 15, "bold"), bg="teal", fg="skyblue").place(
            x=40, y=70)
        #=======username=====
        self.username1 = Label(self.frame2, text="Username", font=("Goudy old style", 20, "bold"), bg="#2C3E4C", fg="#d77337").place(
            x=210, y=110)
        self.ent_username1 = Entry(self.frame2, font=("times new roman", 15), bg="lightgray")
        self.ent_username1.place(x=180, y=150,width=200)


        #=======password=====
        self.password1 = Label(self.frame2, text="Password", font=("Goudy old style", 20, "bold"), bg="#2C3E4C",
                               fg="#d77337").place(
            x=210, y=200)
        self.ent_password1 = Entry(self.frame2, font=("times new roman", 15), bg="lightgray",show="*")
        self.ent_password1.place(x=180, y=240,width=200)
        #=====button========
        self.btn_login=Button(self.wn,text="Login",font=("times new roman",20),fg="white",bg="#d77337",bd=0,cursor="hand2",
                              command=self.login_click).place(x=220,y=320,width=150,height=40)
        #=====forget password====
        self.btn_forget = Button(self.frame2, text="Forget Password ?", font=("Goudy old style", 20, "bold"), fg="white",
                                bg="cadetblue", bd=0, cursor="hand2").place(x=190, y=350)

    def login_click(self):
        #
        # enc_pass = self.ent_password1.get().encode('utf-8')
        # hashed = str(binascii.hexlify(hashlib.pbkdf2_hmac('sha512', enc_pass, b'@ComplexSalt987', 500000))[2:-1])
        # print(hashed)
        # if self.ent_username1.get()=="" or self.ent_password1.get()=="":
        #     messagebox.showerror("Error","please enter username and password",parent=self.wn)
        # else:
        #     username=self.ent_username1.get()
        #     password=hashed
            username = self.ent_username1.get()
            password=self.ent_password1.get()
            query='select * from tbl_register where Username=%s and Password=%s'
            values=(username,password)
            row=self.con_login.select(query,values)


            if row==None:
                messagebox.showerror("error","Invalid username and password",parent=self.wn)

            else:
                messagebox.showinfo("success","congrats login success")
                self.wn.withdraw()
                self.main_window()

        # print(row)
        # print(username)
        # print(password)
    # def register_click(self):
    #     new_window = Toplevel()
    #     Register(new_window)
    #     self.wnn.withdraw()

    def main_window(self):

        new_window=Toplevel()
        Mainwindow(new_window)

window=Tk()
Login(window)
window.mainloop()