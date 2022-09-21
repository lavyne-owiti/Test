import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(self):
         print("setupClass")
    
    @classmethod
    def tearDownClass(self):
         print("teardownClass")
   

    def setUp(self):
        print("setUp")
        self.emp_1=Employee("lavyne","owiti",60000)
        self.emp_2=Employee("Mum","Rech",50000)

    def tearDown(self):
       print("tearDown\n")
        
    def test_email(self):
        print('test_email')

        self.assertEqual(self.emp_1.email,'lavyne.owiti@email.com')
        self.assertEqual(self.emp_2.email,'Mum.Rech@email.com')

        self.emp_1.first='john'
        self.emp_2.first='jane'

        self.assertEqual(self.emp_1.email,'john.owiti@email.com')
        self.assertEqual(self.emp_2.email,'jane.Rech@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname,'lavyne owiti')
        self.assertEqual(self.emp_2.fullname,'Mum Rech')

        self.emp_1.first='john'
        self.emp_2.first='jane'

        self.assertEqual(self.emp_1.fullname,'john owiti')
        self.assertEqual(self.emp_2.fullname,'jane Rech')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise
        self.emp_2.apply_raise

        self.assertEqual(self.emp_1.pay,63000)
        self.assertEqual(self.emp_2.pay,52500)

    # def test_monthly_schedule(self):
    #     with patch('Employee.request.get') as mocked_get:
    #         mocked_get.return_value.ok =True
    #         mocked_get.return_value.text ='Succes'

    #         schedule=self.emp_1.monthly_schedule('May')
    #         mocked_get.assert_called_with('http://company.com/owiti/May')
    #         self.assertEqual(schedule,'Succes')

    #         mocked_get.return_value.ok =False
           

    #         schedule=self.emp_2.monthly_schedule('June')
    #         mocked_get.assert_called_with('http://company.com/Rech/June')
    #         self.assertEqual(schedule,'Bad Response!')
    

if __name__ == '__main__':
    unittest.main()


