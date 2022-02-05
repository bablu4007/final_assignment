class Model_exam:
    def __init__(self,ID,first_name,last_name,marks_obtain,total_marks,percentage):
        self.id=ID
        self.fname=first_name
        self.lname = last_name
        self.marks = marks_obtain
        self.toatl = total_marks
        self.percent = percentage


    def set_ID(self,ID):
        self.id=ID

    def get_ID(self):
        return self.id

    def set_first_name(self, first_name):
        self.fname= first_name

    def get_first_name(self):
        return self.fname

    def set_last_name(self, last_name):
        self.lname = last_name

    def get_last_name(self):
        return self.lname

    def set_marks_obtain(self, marks_obtain):
        self.marks = marks_obtain

    def get_marks_obtain(self):
        return self.marks

    def set_total_marks(self, total_marks):
        self.toatl = total_marks

    def get_total_marks(self):
        return self.toatl

    def set_percentage(self, percentage):
        self.percent = percentage

    def get_percentage(self):
        return self.percent



