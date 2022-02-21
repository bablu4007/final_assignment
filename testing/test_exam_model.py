import  unittest
from model_class1.exam_model import*

class Test_Model_exam(unittest.TestCase):
    def setUp(self):
        self.e=Model_exam(190240,"kiran","Giri",450,500,80)
        self.e1=Model_exam(180124,"anaya","Giri",350,500,60)

    def test_set_marks_obtain(self):
        self.e.set_marks_obtain(480)
        self.assertEqual(480, self.e.get_marks_obtain())

        self.e1.set_marks_obtain(360)
        self.assertEqual(360, self.e1.get_marks_obtain())

    def test_get_marks_obtain(self):
        self.assertEqual(450,self.e.get_marks_obtain())
        self.assertEqual(350, self.e1.get_marks_obtain())

    def test_set_total_marks(self):
        self.e.set_total_marks(500)
        self.assertEqual(500,self.e.get_total_marks())

        self.e1.set_total_marks(800)
        self.assertEqual(800, self.e1.get_total_marks())

    def test_get_total_marks(self):
        self.assertEqual(500,self.e.get_total_marks())
        self.assertEqual(500, self.e1.get_total_marks())


    def tearDown(self):
        self.e=None
