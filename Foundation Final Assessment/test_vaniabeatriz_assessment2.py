import unittest
from vania_beatriz_assessment import squared_number_list


class TestSquareNumber(unittest.TestCase):
    expected = [1, 4, 9, 16, 25, 36, 49]

    def test_squared_number_list(self):
        my_list = [1, 2, 3, 4, 5, 6, 7]
        result = squared_number_list(my_list)
        self.assertListEqual(result, self.expected)



if __name__ == '__main__':
    unittest.main()



