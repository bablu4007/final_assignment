class Model_staff:
    def __init__(self,First_Name,Last_Name,ID_No,Salary,Course_ID,Phone_No,Qualification,Email,DOB,Gender,Subject,Address):

        self.id_no=ID_No
        self.firstname=First_Name
        self.lastname=Last_Name
        self.salary=Salary
        self.dob=DOB
        self.courseid=Course_ID
        self.phoneno=Phone_No
        self.qualification=Qualification
        self.email=Email
        self.gender=Gender
        self.subject=Subject
        self.address=Address
    #====admission date=====

    def set_ID_No(self, ID_No):
        self.id_no = ID_No

    def get_ID_No(self):
        return self.id_no

    def set_First_Name(self, First_Name):
        self.firstname = First_Name

    def get_First_Name(self):
        return self.firstname

    def set_Last_Name(self, Last_Name):
        self.lastname = Last_Name

    def get_Last_Name(self):
        return self.lastname

    def set_Salary(self,Salary):
        self.salary=Salary

    def get_Salary(self):
        return self.salary

    def set_DOB(self, DOB):
        self.dob = DOB

    def get_DOB(self):
        return self.dob

    def set_Course_ID(self, Course_ID):
        self.courseid = Course_ID

    def get_Course_ID(self):
        return self.courseid

    def set_Phone_No(self, Phone_No):
        self.phoneno = Phone_No

    def get_Phone_No(self):
        return self.phoneno

    def set_Qualification(self, Qualification):
        self.qualification = Qualification

    def get_Qualification(self):
        return self.qualification

    def set_Email(self, Email):
        self.email =Email

    def get_Email(self):
        return self.email

    def set_Gender(self, Gender):
        self.gender = Gender

    def get_Gender(self):
        return self.gender

    def set_Subject(self, Subject):
        self.subject = Subject

    def get_Subject(self):
        return self.subject

    def set_Address(self, Address):
        self.address = Address

    def get_Address(self):
        return self.address

