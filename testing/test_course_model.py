import unittest
from model_class1.course_model import*

class Test_Model_course(unittest.TestCase):
    def setUp(self):
        self.c=Model_course(190353,"computing","course related to software and its design ",4)
        self.c1 = Model_course(190240, "Ethical", "course related to cyber and hacking ", 3)
    def test_set_course_id(self):
        self.c.set_course_id(190352)
        self.assertEqual(190352,self.c.get_course_id())

        self.c1.set_course_id(101)
        self.assertEqual(101, self.c1.get_course_id())

    def test_get_course_id(self):
        self.assertEqual(190353,self.c.get_course_id())
        self.assertEqual(190240, self.c1.get_course_id())

    def test_set_course_name(self):
        self.c.set_course_name("MBA")
        self.assertEqual("MBA",self.c.get_course_name())

        self.c1.set_course_name("BBA")
        self.assertEqual("BBA", self.c1.get_course_name())

    def test_get_course_name(self):
        self.assertEqual("computing",self.c.get_course_name())
        self.assertEqual("Ethical", self.c1.get_course_name())


    def tearDown(self):
        self.c=None





