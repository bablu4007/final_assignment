import unittest
from model_class1.register_model import*

class Test_Model_register(unittest.TestCase):
    def setUp(self):
        self.r = Model_register("kiran", "Giri", 9808420246, "kiran123", "abc", "your best friend name", "priya")
        self.r1 = Model_register("anushka", "Giri",9816280241, "anushka123", "anu", "your best friend name", "kiran")

    def test_set_firstname(self):
        self.r.set_firstname("anushka")
        self.assertEqual("anushka",self.r.get_firstname())
        self.r1.set_firstname("ananya")
        self.assertEqual("ananya",self.r1.get_firstname())


    def test_get_firstname(self):
        self.assertEqual("kiran",self.r.get_firstname())
        self.assertEqual("anushka",self.r1.get_firstname())

    def test_set_lastname(self):
        self.r.set_lastname("hussain")
        self.assertEqual("hussain",self.r.get_lastname())
        self.r1.set_lastname("Giri")
        self.assertEqual("Giri", self.r1.get_lastname())

    def test_get_lastname(self):
        self.assertEqual("Giri", self.r.get_lastname())
        self.assertEqual("Giri", self.r1.get_lastname())

    def test_set_username(self):
        self.r.set_username("kiran123")
        self.assertEqual("kiran123",self.r.get_username())
        self.r1.set_username("anu123")
        self.assertEqual("anu123", self.r1.get_username())

    def test_get_username(self):
        self.assertEqual("kiran123",self.r.get_username())
        self.assertEqual("anushka123", self.r1.get_username())


    def tearDown(self):
        self.r=None




