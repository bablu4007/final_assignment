class Model_fee:
    def __init__(self,ID_No,First_Name,Last_Name,Total_fees,semester,year,Paid_amount,Due_amount,Paid_date,Modeof_payment):
        self.id_no=ID_No
        self.firstname=First_Name
        self.lastname=Last_Name
        self.Total_fees=Total_fees
        self.semester=semester
        self.year=year
        self.Paid_amount=Paid_amount
        self.Due_amount=Due_amount
        self.Paid_date=Paid_date
        self.Modeof_payment=Modeof_payment


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

    def set_Total_fees(self, Total_fees):
        self.Total_fees = Total_fees

    def get_Total_fees(self):
        return self.Total_fees

    def set_semester(self, semester):
        self.semester = semester

    def get_semester(self):
        return self.semester

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_Paid_amount(self, Paid_amount):
        self.Paid_amount = Paid_amount

    def get_Paid_amount(self):
        return self.Paid_amount

    def set_Due_amount(self, Due_amount):
        self.Due_amount =Due_amount

    def get_Due_amount(self):
        return self.Due_amount

    def set_Paid_date(self, Paid_date):
        self.Paid_date = Paid_date

    def get_Paid_date(self):
        return self.Paid_date

    def set_Modeof_payment(self, Modeof_payment):
        self.Modeof_payment = Modeof_payment

    def get_Modeof_payment(self):
        return self.Modeof_payment



