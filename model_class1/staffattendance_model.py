class Model_staffattendance:
    def __init__(self ,First_Name, Last_Name,ID_No, From, To, Total_days, Days_present, Days_absent):
        self.id_no = ID_No
        self.firstname = First_Name
        self.lastname = Last_Name
        self.From = From
        self.To = To
        self.Total_days = Total_days
        self.Days_present = Days_present
        self.Days_absent = Days_absent

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

    def set_From(self, From):
        self.From = From

    def get_From(self):
        return self.From

    def set_To(self, To):
        self.To = To

    def get_To(self):
        return self.To

    def set_Total_days(self, Total_days):
        self.Total_days = Total_days

    def get_Total_days(self):
        return self.Total_days

    def set_Days_present(self, Days_present):
        self.Days_present = Days_present

    def get_Days_present(self):
        return self.Days_present

    def set_Days_absent(self, Days_absent):
        self.Days_absent = Days_absent

    def get_Days_absent(self):
        return self.Days_absent

