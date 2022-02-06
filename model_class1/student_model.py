class Model_student:
    def __init__(self,Admission_date,ID_No,First_Name,Last_Name,DOB,Course_ID,Phone_No,Father_Name,Mother_Name,Gender,Section,Address):
        self.admissiondate=Admission_date
        self.id_no=ID_No
        self.firstname=First_Name
        self.lastname=Last_Name
        self.dob=DOB
        self.courseid=Course_ID
        self.phoneno=Phone_No
        self.fathername=Father_Name
        self.mothername=Mother_Name
        self.gender=Gender
        self.section=Section
        self.address=Address
    #====admission date=====
    def set_Admission_date(self,Admission_date):
        self.admissiondate=Admission_date

    def get_Admission_date(self):
        return self.admissiondate

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

    def set_Father_Name(self, Father_Name):
        self.fathername = Father_Name

    def get_Father_Name(self):
        return self.fathername

    def set_Mother_Name(self, Mother_Name):
        self.mothername =Mother_Name

    def get_Mother_Name(self):
        return self.mothername

    def set_Gender(self, Gender):
        self.gender = Gender

    def get_Gender(self):
        return self.gender

    def set_Section(self, Section):
        self.section = Section

    def get_Section(self):
        return self.section

    def set_Address(self, Address):
        self.address = Address

    def get_Address(self):
        return self.address

