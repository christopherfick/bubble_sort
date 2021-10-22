import unittest
from bubblesort import bubble_sort 

class TestMain(unittest.TestCase):

    def test_main(self):
       self.assertEqual(bubble_sort([5,4,3,2,1]), [1,2,3,4,5])


if __name__ == '__main__':
    unittest.main()
