import unittest
from front_end1.Course_section import *


class Test_Course(unittest.TestCase):
    def setUp(self):
        self.data = ["CA", "MBA", "BBA", "Bsc.computing"]
        self.data1 = ["1", "BBS", "BBA", "Bsc.computing"]
        self.item = "CA"
        self.item1 = "Ethical"
        self.item3 = 1
        self.item4 = 5

    def test_linear_search(self):
        self.assertTrue(Course.linear_search(self.data, self.item))
        self.assertFalse(Course.linear_search(self.data, self.item1))

        self.assertTrue(Course.linear_search(self.data1, self.item3))
        self.assertFalse(Course.linear_search(self.data1, self.item4))

    def test_bubblesort_ascending(self):
        self.list1 = [2, 4, 1, 12, 10]
        self.list2 = ["Ram", "Shyam", "Armaan"]
        expected = ["Armaan", "Ram", "Shyam"]
        actual = Course.bubblesort_ascending(self.list2)
        self.assertEqual(expected, actual)

    def tearDown(self):
        self.data = None
        self.data1 = None

