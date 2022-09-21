import unittest
import operations

class Testoperations(unittest.TestCase):

    def test_add(self):
        # result= operations.add(10,5)
        self.assertEqual(operations.add(10,5),15)
        self.assertEqual(operations.add(-1,1),0)
        self.assertEqual(operations.add(-1,-1),-2)

    def test_sub(self):
        # result= operations.add(10,5)
        self.assertEqual(operations.sub(10,5),5)
        self.assertEqual(operations.sub(-1,1),-2)
        self.assertEqual(operations.sub(-1,-1),0)

    def test_mutl(self):
        # result= operations.add(10,5)
        self.assertEqual(operations.mult(10,5),50)
        self.assertEqual(operations.mult(-1,1),-1)
        self.assertEqual(operations.mult(-1,-1),1)

    def test_divide(self):
        # result= operations.add(10,5)
        self.assertEqual(operations.divide(10,5),2)
        self.assertEqual(operations.divide(-1,1),-1)
        self.assertEqual(operations.divide(-1,-1),1)
        self.assertEqual(operations.divide(5,2),2.5)
        self.assertEqual(operations.divide(5,0),2.5)

        # use context method when testing exceptions
        with self.assertRaises(ValueError):
            operations.divide(10,0)

if __name__ == '__main__':
    unittest.main()