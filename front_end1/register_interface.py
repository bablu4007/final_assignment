from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import hashlib,binascii
from front_end1.login_interface import *
from tkinter import messagebox
from model_class1.register_model import*
from back_end1.register_connection import*
class Register:
    def __init__(self,screen):
        self.wnn=screen
        self.wnn.geometry("1470x840+60+0")
        self.wnn.title("Registration window".center(450))
        self.wnn.resizable(0, 0)
        #self.wn.configure(background="cyan")
        self.con_register=register_database()
        #====background image=========
        self.canvas1 = Canvas(self.wnn, width=1470, height=840, bg="black")
        self.canvas1.place(x=0, y=0)
        self.photo = PhotoImage(file="C:\\Users\\Bablu\\pythonProject\\final_assignment_semIII\\images\\color.png")
        self.canvas1.create_image(0, 0, image=self.photo, anchor=NW)
        #self.bg=b
        #self.bg_image=Label(self.wn,databseimage=self.bg).place(x=80,y=100,width=400,height=500)
        #====frame====
        self.frame1=Frame(self.wnn,bg="moccasin")
        self.frame1.place(x=766,y=0,width=700,height=840)

        self.title=Label(self.frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="moccasin",fg="navy").place(x=50,y=30)
        self.f_name = Label(self.frame1, text="First Name", font=("times new roman", 17, "bold"), bg="moccasin",
                           fg="darkolivegreen").place(x=50, y=100)
        self.ent_fname=Entry(self.frame1,font=("times new roman",15),bg="lightgray")
        self.ent_fname.place(x=50,y=130,width=250)
        #=======lastname====
        self.l_name = Label(self.frame1, text="Last Name", font=("times new roman", 17, "bold"), bg="moccasin",
                            fg="darkolivegreen").place(x=370, y=100)
        self.ent_lname = Entry(self.frame1, font=("times new roman", 15), bg="lightgray")
        self.ent_lname.place(x=370, y=130, width=250)

        #======contact no==========
        self.contact_no = Label(self.frame1, text="Contact_No.", font=("times new roman", 17, "bold"), bg="moccasin",
                            fg="darkolivegreen").place(x=50, y=200)
        self.ent_contactno = Entry(self.frame1, font=("times new roman", 15), bg="lightgray")
        self.ent_contactno.place(x=50, y=230, width=250)
        #=======username=========
        self.username = Label(self.frame1, text="Username", font=("times new roman", 17, "bold"), bg="moccasin",
                            fg="darkolivegreen").place(x=370, y=200)
        self.ent_username = Entry(self.frame1, font=("times new roman", 15), bg="lightgray")
        self.ent_username.place(x=370, y=230, width=250)
        #=======password=====
        self.password = Label(self.frame1, text="Password", font=("times new roman", 17, "bold"), bg="moccasin",
                           fg="darkolivegreen").place(x=50, y=300)
        self.ent_password = Entry(self.frame1, font=("times new roman", 15), bg="lightgray",show="*")
        self.ent_password.place(x=50, y=340, width=250)
        #===confirm password======
        self.conpassword = Label(self.frame1, text="Confirm Password", font=("times new roman", 17, "bold"), bg="moccasin",
                           fg="darkolivegreen").place(x=370, y=300)
        self.ent_confirmpass = Entry(self.frame1, font=("times new roman", 15), bg="lightgray",show="*")
        self.ent_confirmpass.place(x=370, y=340, width=250)
        #========security question======
        self.security = Label(self.frame1, text="Security Question", font=("times new roman", 17, "bold"), bg="moccasin",
                                 fg="darkolivegreen").place(x=50, y=400)

        self.combox=ttk.Combobox(self.frame1,font=("times new roman",15))
        self.combox['values']=("Select","Your Favourite pet name","Your birth place","Your best friend name","Your Favorite movie", "Your Favorite "
                                                                                                                                    "football team")
        self.combox.place(x=50,y=435,width=250)



        #==========Answer=======
        self.answer = Label(self.frame1, text="Answer", font=("times new roman", 17, "bold"), bg="moccasin",
                                 fg="darkolivegreen").place(x=370, y=400)
        self.ent_answer = Entry(self.frame1, font=("times new roman", 15), bg="lightgray")
        self.ent_answer.place(x=370, y=435,width=250)
        #======checkbox terms and conditino=====
        self.check_var=IntVar()
        self.check=Checkbutton(self.frame1,text="I agree the terms and conditions.",variable=self.check_var,onvalue=1,offvalue=0,
                               fg="black",bg="moccasin",font=("times new roman",17,"bold")).place(x=50,y=540)
        #=======button=======
        self.btn_register=Button(self.frame1,text="REGISTER  NOW",font=("times new roman",15,"bold"),fg="white",bg="green",
                                 bd=5,relief=GROOVE,cursor="hand2",command=self.register_click).place(x=250,y=620)
        #======already account label====
        self.lbl_already=Label(self.frame1,text="Already have an account ?",font=("Goudy old style",20,"bold"),
                               bg="moccasin",fg="darkred").place(x=180,y=700)
        self.btn_login = Button(self.frame1, text="Login Here", font=("Goudy old style", 20, "bold"), fg="navy",
                                bg="moccasin", bd=0, command=self.login_click, cursor="hand2").place(x=470,y=697)

    def login_click(self):
        new_window=Toplevel()
        Login(new_window)
        self.wnn.withdraw()


    def register_click(self):
        # entered_password = self.ent_password.get()
        # enc_pass = entered_password.encode('utf-8')
        # hashed = str(
        #     binascii.hexlify(hashlib.pbkdf2_hmac('sha512', enc_pass, b'@ComplexSalt987', 500000))[2:-1])

        if self.ent_fname.get()==""or self.ent_contactno.get()=="" or self.ent_username.get()=="" or self.ent_password.get()=="" or self.ent_confirmpass.get()=="" or self.combox.get()=="" or self.ent_answer.get()=="":
            messagebox.showerror("Error","All fields are required ")

        elif self.ent_password.get()!=self.ent_confirmpass.get():
            messagebox.showerror("Error", "Password and confirm password must be same")
        elif self.check_var.get()==0:
            messagebox.showerror("Error","Please agree the terms and condition..")
        elif self.ent_fname.get().isdigit() or self.ent_lname.get().isdigit() or self.ent_answer.get().isdigit():
            messagebox.showerror("error","integer value is not allowed in first name ,last name and answer")

        elif self.ent_contactno.get().isalpha():
            messagebox.showerror("Error","String value is not allowed in contact number, please enter numbers only")
        else:
            try:
                Registry_obj=Model_register(self.ent_fname.get(),self.ent_lname.get(),self.ent_contactno.get(),self.ent_username.get()
                                            ,self.ent_password.get(),self.combox.get(),self.ent_answer.get())
                query="insert into tbl_register values(%s,%s,%s,%s,%s,%s,%s);"
                values=(Registry_obj.get_firstname(),Registry_obj.get_lastname(),Registry_obj.get_contact(),Registry_obj.get_username()
                        ,Registry_obj.get_password(),Registry_obj.get_securityques(),Registry_obj.get_answer())
                self.con_register.insert(query,values)
                messagebox.showinfo("Success", " thanks for creating account ")
                self.ent_fname.delete(0,END),self.ent_lname.delete(0,END),self.ent_contactno.delete(0,END),self.ent_username.delete(0,END),self.ent_password.delete(0,END),
                self.ent_confirmpass.delete(0,END),self.combox.delete(0,END),self.ent_answer.delete(0,END)

            except Exception as es:
                messagebox.showerror("error",f"error due to {str(es)}")



window=Tk()
Register(window)
window.mainloop()


