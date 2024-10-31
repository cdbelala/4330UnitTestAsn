import unittest
from sortAlg import quicksort

class quicksortTest(unittest.TestCase):
    def testEmpty(self):
        self.assertEqual(quicksort([]), [])
    def testOneElem(self):
        self.assertEqual(quicksort([1]), [1])
    def testSorted(self):
        self.assertEqual([1, 2, 3, 4, 5]), ([1, 2, 3, 4, 5])
    def testDupes(self):
        self.assertEqual(quicksort([3, 3, 3, 3]), [3, 3, 3, 3])
    def testManyRuns(self):
        arr = [3, 6, 8, 10, 1, 2, 1]
        sortOnce = quicksort(arr)
        sortTwice = quicksort(sortOnce)
        self.assertEqual(sortOnce, sortTwice)
    def testIsString(self):
        with self.assertRaises(TypeError):
            quicksort([9, "o", 3])
