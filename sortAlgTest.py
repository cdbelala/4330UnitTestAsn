import unittest
from sortAlg import quicksort

class quicksortTest(unittest.TestCase):
    def testEmptyList(self):
        self.assertEqual(quicksort([]), [])
    def testOneElement(self):
        self.assertEqual(quicksort([1]), [1])
    def testSorted(self):
        self.assertEqual([1, 2, 3, 4, 5]), ([1, 2, 3, 4, 5])
    def test_with_duplicates(self):
        self.assertEqual(quicksort([3, 3, 3, 3]), [3, 3, 3, 3])
