import mysql.connector
class register_database:
    def __init__(self):
        self.con1=mysql.connector.connect(host='localhost', user='root', password='',database='finalproject')
        self.cursor1=self.con1.cursor()

    def insert(self,query,values):
        self.cursor1.execute(query,values)
        self.con1.commit()
    def select(self,query,values):
        self.cursor1.execute(query,values)
        row=self.cursor1.fetchone()
        self.con1.commit()
        return row
    def update(self,query,value):
        self.cursor1.execute(query,value)
        self.con1.commit()
    def delete(self,query,value):
        self.cursor1.execute(query,value)
        self.con1.commit()
    def select1(self,query):
        self.cursor1.execute(query)
        row = self.cursor1.fetchall()
        self.con1.commit()
        return row
