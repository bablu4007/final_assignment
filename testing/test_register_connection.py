import unittest
from back_end1.register_connection import*
class Test_register_connection(unittest.TestCase):
    def setUp(self):
        self.query="insert into tbl_course values(%s,%s,%s,%s);"
        self.values=(1,"CA","this is account or business related course",5)
        self.query1="delete * from tbl_course where Course_ID=%s;"
        self.dbconnect=register_database()

    def test_insert(self):
        self.dbconnect.insert(self.query,self.values)
        expect=[(1,"CA","this is account or business related course",5),]
        actual="select * from tbl_course where Course_ID=%s;"
        self.assertEqual(expect,actual)

    def tearDown(self):
        self.values=None

