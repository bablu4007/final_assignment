class Model_register:
    def __init__(self,firstname,lastname,contact,username,password,securityques,answer):
        self.fname=firstname
        self.lname=lastname
        self.contact = contact
        self.username = username
        self.password = password
        self.security = securityques
        self.ans = answer

    def set_firstname(self,firstname):
        self.fname=firstname

    def get_firstname(self):
        return self.fname

    def set_lastname(self, lastname):
        self.lname = lastname

    def get_lastname(self):
        return self.lname

    def set_contact(self, contact):
        self.contact = contact

    def get_contact(self):
        return self.contact

    def set_username(self, username):
        self.username = username

    def get_username(self):
        return self.username

    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    def set_securityques(self, securityques):
        self.security = securityques

    def get_securityques(self):
        return self.security

    def set_answer(self, answer):
        self.ans = answer

    def get_answer(self):
        return self.ans

