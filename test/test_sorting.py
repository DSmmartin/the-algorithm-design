import unittest

from problems.sorting import sorting

class TestSortign(unittest.TestCase):
    def test_sorting(self):
        data = [9, 4, 5, 6, 4]
        result = sorting(data)
        self.assertListEqual(result, [4, 4, 5, 6, 9])

if __name__ == '__main__':
    unittest.main()
