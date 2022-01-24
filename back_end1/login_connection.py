# import mysql.connector
# class login_database:
#     def __init__(self):
#         self.con2=mysql.connector.connect(host='localhost', user='root', password='',
#                                       database='university')
#         self.cursor2=self.con2.cursor()
#
#     def select(self,query,values):
#         self.cursor2.execute(query,values)
#         row=self.cursor2.fetchone()
#         self.con2.commit()
#         return row